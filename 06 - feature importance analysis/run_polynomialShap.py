#!/usr/bin/env python3

import configparser
import json

import joblib
import numpy as np
import pandas as pd
import shap



data = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
data.read('data.ini')
data = data['DEFAULT']

with open(data['ml'] + 'tools_features_selection.json', 'r') as file:
    features_selections = json.load(file)

features_selections_genes = {}
for key, value in features_selections.items():
    features_selections_genes[key] = value['genes']


# TCGA_tran&mut_["mutclust - ALL"]_["maxmifHN S - onlyRAS_onlyNonRAS"]_randomForest_shapValues

suffix = 'TCGA_tran&mut_["mutclust - ALL"]'
modelsDir = f"{data['ml___models']}optimized_accuracy/{suffix}"
inputDir = f"{data['ml___input']}{suffix}"
key = 'maxmif HN S - onlyRAS_onlyNonRAS'

model_pSVM_maxmifHN_mutclust = joblib.load(f'{modelsDir}/[\"{key}\"]/randomForest.joblib')

scaler = joblib.load(f'{modelsDir}/[\"{key}\"]/scaler.joblib')

with open(f'{modelsDir}/[\"{key}\"]/features_info.json') as f:
    info_maxmifHN_mutclust = json.load(f)

train_RAS = pd.read_csv(f'{inputDir}/train_RAS.csv', sep=',', comment='#', engine='python')
train_nonRAS = pd.read_csv(f'{inputDir}/train_nonRAS.csv', sep=',', comment='#', engine='python')
test_RAS = pd.read_csv(f'{inputDir}/test_RAS.csv', sep=',', comment='#', engine='python')
test_nonRAS = pd.read_csv(f'{inputDir}/test_nonRAS.csv', sep=',', comment='#', engine='python')


train_maxmifHN_mutclust = scaler.transform(pd.concat([train_RAS, train_nonRAS])[info_maxmifHN_mutclust['valid_features_train']])
test_maxmifHN_mutclust = scaler.transform(pd.concat([test_RAS, test_nonRAS])[info_maxmifHN_mutclust['valid_features_train']])


print('mutclust - Calculating SHAP values...')
shapValues = shap.KernelExplainer(model_pSVM_maxmifHN_mutclust.predict,  shap.kmeans(train_maxmifHN_mutclust, 50)).shap_values(test_maxmifHN_mutclust)

np.save('shap/TCGA_tran&mut_["mutclust - ALL"]_["maxmifHN S - onlyRAS_onlyNonRAS"]_randomForest_shapValues.npy', shapValues)


# merged_mut_["mutclust - ALL"]_["maxmifHN S - onlyRAS_onlyNonRAS"]_randomForest_shapValues

suffix = 'merged_mut_["mutclust - ALL"]'
modelsDir = f"{data['ml___models']}optimized_accuracy/{suffix}"
inputDir = f"{data['ml___input']}{suffix}"
key = 'maxmif HN S - onlyRAS_onlyNonRAS'

model_pSVM_maxmifHN_mutclust = joblib.load(f'{modelsDir}/[\"{key}\"]/randomForest.joblib')

scaler = joblib.load(f'{modelsDir}/[\"{key}\"]/scaler.joblib')

with open(f'{modelsDir}/[\"{key}\"]/features_info.json') as f:
    info_maxmifHN_mutclust = json.load(f)

train_RAS = pd.read_csv(f'{inputDir}/train_RAS.csv', sep=',', comment='#', engine='python')
train_nonRAS = pd.read_csv(f'{inputDir}/train_nonRAS.csv', sep=',', comment='#', engine='python')
test_RAS = pd.read_csv(f'{inputDir}/test_RAS.csv', sep=',', comment='#', engine='python')
test_nonRAS = pd.read_csv(f'{inputDir}/test_nonRAS.csv', sep=',', comment='#', engine='python')


train_maxmifHN_mutclust = scaler.transform(pd.concat([train_RAS, train_nonRAS])[info_maxmifHN_mutclust['valid_features_train']])
test_maxmifHN_mutclust = scaler.transform(pd.concat([test_RAS, test_nonRAS])[info_maxmifHN_mutclust['valid_features_train']])


print('mutclust - Calculating SHAP values...')
shapValues = shap.KernelExplainer(model_pSVM_maxmifHN_mutclust.predict,  shap.kmeans(train_maxmifHN_mutclust, 50)).shap_values(test_maxmifHN_mutclust)

np.save('shap/merged_mut_["mutclust - ALL"]_["maxmifHN S - onlyRAS_onlyNonRAS"]_randomForest_shapValues.npy', shapValues)
