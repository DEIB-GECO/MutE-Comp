import json
import os
import sys

import joblib
from joblib import parallel_backend
import pandas as pd
from sklearn.preprocessing import StandardScaler



from models import logistic_regression, lasso_logistic_regression, linear_svm, polynomial_svm, random_forest
from parse_expression import expression_to_tree_and_evaluate


def prepare_data(features_selections_obj, train_RAS, train_nonRAS, feature, saveDir, transcriptomics_non_filtered=False):

    features_selections_genes = {}
    for key, value in features_selections_obj.items():
        features_selections_genes[key] = value['genes']

    # construct train data
    x_train = pd.concat([train_RAS, train_nonRAS])
    y_train = [1] * len(train_RAS) + [0] * len(train_nonRAS)

    # select feature to use
    if feature != '"noFeatureSelection"':
        selected_features = list(expression_to_tree_and_evaluate(feature, features_selections_genes))
        if transcriptomics_non_filtered == False:
            valid_features_train = [feature for feature in x_train.columns if any(feature.startswith(allowed + '_') or feature == allowed for allowed in selected_features)]
        else:
            valid_features_train = [feature for feature in x_train.columns if feature.endswith('_tran') or any(feature.startswith(allowed + '_') or feature == allowed for allowed in selected_features)]
    else:
        valid_features_train = [feature for feature in x_train.columns if feature != 'Sample']

    # Select only the valid features
    x_train = x_train[valid_features_train]

    # check if there are all zero rows and remove them
    x_train = x_train.reset_index(drop=True)
    zero_rows = x_train.index[x_train.eq(0).all(1)]
    x_train = x_train.drop(zero_rows)
    y_train = [y_train[i] for i in range(len(y_train)) if i not in zero_rows]

    # check if there are NaN values and remove them
    x_train = x_train.reset_index(drop=True)
    nan_rows = x_train.isna().any(axis=1)
    x_train = x_train[~nan_rows]
    y_train = [y_train[i] for i in range(len(y_train)) if not nan_rows[i]]

    x_train = x_train.reset_index(drop=True)

    # normalize
    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    
    with open(f'{saveDir}/features_info.json', 'w') as file:
        json.dump({'features': feature, 'valid_features_train': valid_features_train}, file, indent=4)

    # save scaler
    joblib.dump(scaler, f'{saveDir}/scaler.joblib')

    return x_train, y_train


def run_models(data_ini, features_selections, features, clusters, transcriptomics_non_filtered, optimize):

    for cluster in clusters:

        # load input data
        train_RAS = pd.read_csv(f"../{data_ini['ml___input']}{cluster}/train_RAS.csv", sep=',', comment='#', engine='python')
        train_nonRAS = pd.read_csv(f"../{data_ini['ml___input']}{cluster}/train_nonRAS.csv", sep=',', comment='#', engine='python')

        for feature in features:
            
            # create save directory
            if transcriptomics_non_filtered == False:
                saveDir = f"../{data_ini['ml___models']}optimized_{optimize}/{cluster}/[{feature}]"
            else:
                saveDir = f"../{data_ini['ml___models']}optimized_{optimize}/{cluster}_allTran/[{feature}]"
            if not os.path.exists(saveDir):
                os.makedirs(saveDir)
            
            # clean and prepare train data
            x_train, y_train = prepare_data(features_selections, train_RAS, train_nonRAS, feature, saveDir, transcriptomics_non_filtered)
            
            for name, fun in [('logisticRegression', logistic_regression),
                              ('logisticRegressionLasso', lasso_logistic_regression),
                              ('linearSVM', linear_svm),
                              ('polynomialSVM', polynomial_svm),
                              ('randomForest', random_forest)]:
                
                print(f'\t{cluster} : [{feature}] : {name}', flush=True)
                sys.stdout.flush()

                with parallel_backend('threading', n_jobs=8):
                    # perform grid search and train models
                    model, grid = fun(x_train, y_train, optimize, int(data_ini['seed']))

                # save model and grid
                joblib.dump(model, f'{saveDir}/{name}.joblib')
                joblib.dump(grid, f'{saveDir}/{name}_gridsearch.joblib')
