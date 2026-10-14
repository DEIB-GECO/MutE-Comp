import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import matthews_corrcoef, make_scorer
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC



mcc = make_scorer(matthews_corrcoef)


def logistic_regression(x_train, y_train, optimize, seed):
    if optimize == 'mcc':
        optimize = mcc
    grid_params_LR = {}
    cv = KFold(n_splits=5, shuffle=True, random_state=seed)
    logisticRegression = LogisticRegression(solver="newton-cg", max_iter=10000, penalty=None, random_state=seed)
    grid_search_LR = GridSearchCV(logisticRegression, grid_params_LR, cv=cv, scoring=optimize, refit=True)
    grid_search_LR.fit(x_train, y_train)
    return grid_search_LR.best_estimator_, grid_search_LR


def lasso_logistic_regression(x_train, y_train, optimize, seed):
    if optimize == 'mcc':
        optimize = mcc
    s = -3
    e = 5
    grid_params_LRl = {'C': np.logspace(s, e, (e-s)*10+1)[::-1]} # reversed to get less regularized as best in case of tie
    cv = KFold(n_splits=5, shuffle=True, random_state=seed)
    LogisticRegressionLasso_cv = LogisticRegression(penalty='l1', solver='liblinear', n_jobs=1, max_iter=10000, random_state=seed) # n_jobs=1 because of liblinear solver
    grid_search_LRl = GridSearchCV(LogisticRegressionLasso_cv, grid_params_LRl, cv=cv, scoring=optimize, refit=True)
    grid_search_LRl.fit(x_train, y_train)    
    return grid_search_LRl.best_estimator_, grid_search_LRl


def linear_svm(x_train, y_train, optimize, seed):
    if optimize == 'mcc':
        optimize = mcc
    s = -3
    e = 5
    grid_params_lSVM = {'C': np.logspace(s, e, (e-s)*10+1)[::-1]} # reversed to get less regularized as best in case of tie
    cv = KFold(n_splits=5, shuffle=True, random_state=seed)
    linearSVM_cv = SVC(kernel='linear', max_iter=100000000, random_state=seed)
    grid_search_lSVM = GridSearchCV(linearSVM_cv, grid_params_lSVM, cv=cv, scoring=optimize, refit=True)
    grid_search_lSVM.fit(x_train, y_train)
    return grid_search_lSVM.best_estimator_, grid_search_lSVM


def polynomial_svm(x_train, y_train, optimize, seed):
    if optimize == 'mcc':
        optimize = mcc
    s = -3
    e = 5
    grid_params_pSVM = {'C': np.logspace(s, e, (e-s)*1+1)[::-1], # reversed to get less regularized as best in case of tie
                    'degree': np.arange(2, 6, 1),
                    'coef0': np.logspace(-3, 2, 6)}
    cv = KFold(n_splits=5, shuffle=True, random_state=seed)
    polynomialSVM_cv = SVC(kernel='poly', max_iter=100000000, random_state=seed)
    grid_search_pSVM = GridSearchCV(polynomialSVM_cv, grid_params_pSVM, cv=cv, scoring=optimize, refit=True)
    grid_search_pSVM.fit(x_train, y_train)
    return grid_search_pSVM.best_estimator_, grid_search_pSVM


def random_forest(x_train, y_train, optimize, seed):
    if optimize == 'mcc':
        optimize = mcc
    grid_params_RF = {'n_estimators': np.arange(1, 100, 20),
                    'min_samples_split': np.arange(2, 60, 10),
                    'max_features': ['sqrt', 'log2']}
    cv = KFold(n_splits=5, shuffle=True, random_state=seed)
    randomForest_cv = RandomForestClassifier(random_state=seed)
    grid_search_RF = GridSearchCV(randomForest_cv, grid_params_RF, cv=cv, scoring=optimize, refit=True)
    grid_search_RF.fit(x_train, y_train)
    return grid_search_RF.best_estimator_, grid_search_RF
