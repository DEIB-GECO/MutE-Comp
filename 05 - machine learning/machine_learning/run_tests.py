import json
import os
import re

import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, matthews_corrcoef, precision_score, recall_score
from sklearn.utils import shuffle



def parseModelType(name: str):
    splits = name.split('_')
    dataset = splits[0]
    dataType = splits[1]

    clusters = re.findall(r'\[(.*?)\]', name)
    if len(clusters) > 0:
        clusters = clusters[0]                                  # e.g. '["tool0 - on0" + "tool1 - on1"]'
        clusters_types = re.findall(r'\"(.*?)\"', clusters)     # e.g. ['tool0 - on0', 'tool1 - on1']
        clusters_tools = []
        clusters_tools_on =[]
        for tool in clusters_types:
            clusters_tools.append(tool.split(' - ')[0])         # e.g. ['tool0', 'tool1']
            clusters_tools_on.append(tool.split(' - ')[1])      # e.g. ['on0', 'on1']
        clusters_tool = ', '.join(clusters_tools)
        clusters_tool_on = ', '.join(clusters_tools_on)
    else:
        clusters_tool = ''
        clusters_tool_on = ''

    input_name = name
    isTranFiltered = None
    if 'tran' in dataType.lower():
        if name.endswith('allTran'):
            isTranFiltered = False
            input_name = name[:-8]
        else:
            isTranFiltered = True

    return input_name, dataset, dataType, clusters_tool, clusters_tool_on, isTranFiltered


def preprocess_test_data(model_type_path, seed, train_RAS, train_nonRAS, test_RAS, test_nonRAS):

    with open(f'{model_type_path}/features_info.json', 'r') as file:
            features_info = json.load(file)
    valid_features_train = features_info['valid_features_train']

    x_train = pd.concat([train_RAS, train_nonRAS])
    
    x_test = pd.concat([test_RAS, test_nonRAS])
    y_test = [1] * len(test_RAS) + [0] * len(test_nonRAS)

    numTest = len(x_test)
    numTrain = len(x_train)

    x_train = x_train[valid_features_train]
    x_test = x_test[valid_features_train]
    
    # check if there are all zero rows and remove them
    x_test = x_test.reset_index(drop=True)
    zero_rows = x_test.index[x_test.eq(0).all(1)]
    x_test = x_test.drop(zero_rows)
    y_test = [y_test[i] for i in range(len(y_test)) if i not in zero_rows]

    x_train = x_train.reset_index(drop=True)
    zero_rows_train = x_train.index[x_train.eq(0).all(1)]
    x_train = x_train.drop(zero_rows_train)

    x_test = x_test.reset_index(drop=True)

    numValidFeatures = len(x_train.columns)
    numValidTest = len(x_test)
    numValidTrain = len(x_train)
    perValidTest = numValidTest / numTest * 100
    perValidTrain = numValidTrain / numTrain * 100

    x_test, y_test = shuffle(x_test, y_test, random_state=seed)

    # normalize
    scaler = joblib.load(f'{model_type_path}/scaler.joblib')
    x_test = scaler.transform(x_test)

    return x_test, y_test, {'numFeature': numValidFeatures, 'numTrain': numTrain, 'numTest': numTest, 'numValidTrain': numValidTrain, 'numValidTest': numValidTest, 'perValidTrain': perValidTrain, 'perValidTest': perValidTest}


def run_tests(data_ini, model_types, optimized_by, out):

    results = pd.DataFrame()

    for model_type in model_types:

        input_name, dataset, dataType, clusters_tool, clusters_tool_on, isTranFiltered = parseModelType(model_type)

        # load input data
        train_RAS = pd.read_csv(f"../{data_ini['ml___input']}{input_name}/train_RAS.csv", sep='\t', comment='#', engine='python')
        train_nonRAS = pd.read_csv(f"../{data_ini['ml___input']}{input_name}/train_nonRAS.csv", sep='\t', comment='#', engine='python')
        test_RAS = pd.read_csv(f"../{data_ini['ml___input']}{input_name}/test_RAS.csv", sep='\t', comment='#', engine='python')
        test_nonRAS = pd.read_csv(f"../{data_ini['ml___input']}{input_name}/test_nonRAS.csv", sep='\t', comment='#', engine='python')

        # cicle on folders in the model directory
        for featureSelection_dir in os.listdir(f"../{data_ini['ml___models']}optimized_{optimized_by}/{model_type}"):
            tool = featureSelection_dir.strip('[]"').split(' - ')[0]
            try:
                tool_on = featureSelection_dir.strip('[]"').split(' - ')[1]
            except IndexError:
                tool_on = ''

            featureSelection_dir = os.path.join(f"../{data_ini['ml___models']}optimized_{optimized_by}/{model_type}", featureSelection_dir)

            # preprocess test data
            x_test, y_test, info = preprocess_test_data(featureSelection_dir, int(data_ini['seed']), train_RAS, train_nonRAS, test_RAS, test_nonRAS)

            # load model
            for model_name in ['logisticRegression',
                              'logisticRegressionLasso',
                              'linearSVM',
                              'polynomialSVM',
                              'randomForest']:
                
                if not os.path.exists(f'{featureSelection_dir}/{model_name}.joblib'):
                    continue

                # print(f'\t{model_type} : {featureSelection_dir} : {model_name}', flush=True)

                model = joblib.load(f'{featureSelection_dir}/{model_name}.joblib')
                grid = joblib.load(f'{featureSelection_dir}/{model_name}_gridsearch.joblib')

                y_pred = model.predict(x_test)
                num_splits = len([key for key in grid.cv_results_.keys() if key.startswith('split') and key.endswith('_test_score')])

                result = pd.DataFrame([{
                    'dataset': dataset,
                    'data': dataType,
                    'model': model_name,
                    'genes tool': tool,
                    'genes tool set': tool_on,
                    'isTranFiltered': ('yes' if isTranFiltered else ('no' if isTranFiltered is False else '')),
                    'clusters tool': clusters_tool,
                    'cluster tool set': clusters_tool_on,
                    '#features': info['numFeature'],
                    '#nonZeroParams_lasso': str((model.coef_ != 0).sum()) if 'lasso' in model_name.lower() else '',
                    'mean cv metric': grid.best_score_,
                    'std cv metric': grid.cv_results_['std_test_score'][grid.best_index_],
                    'median cv metric': np.median([grid.cv_results_[f'split{i}_test_score'][grid.best_index_] for i in range(num_splits)]),
                    'accuracy': accuracy_score(y_test, y_pred),
                    'precision nonRAS': precision_score(y_test, y_pred, average=None, labels=[0,1], zero_division=0)[0],
                    'precision RAS': precision_score(y_test, y_pred, average=None, labels=[0,1], zero_division=0)[1],
                    'recall nonRAS': recall_score(y_test, y_pred, average=None, labels=[0,1], zero_division=0)[0],
                    'recall RAS': recall_score(y_test, y_pred, average=None, labels=[0,1], zero_division=0)[1],
                    'f1 nonRAS': f1_score(y_test, y_pred, average=None, labels=[0,1], zero_division=0)[0],
                    'f1 RAS': f1_score(y_test, y_pred, average=None, labels=[0,1], zero_division=0)[1],
                    'MCC': matthews_corrcoef(y_test, y_pred),
                    '#train sample': info['numValidTrain'],
                    '#test sample': info['numValidTest'],
                    '%train sample': info['perValidTrain'],
                    '%test sample': info['perValidTest'],
                    '#iterations': model.n_iter_[0] if model_name != 'randomForest' else '',
                    'best params': grid.best_params_,
                    'grid optimized': optimized_by
                }])

                results = pd.concat([results, result], ignore_index=True)

    results.to_csv(f"../{data_ini['ml___results']}{out}", sep='\t', index=True)
