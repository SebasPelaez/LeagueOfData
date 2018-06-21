from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier

def Selector(value):
    estimator = switcher.get(value, "nothing")
    return estimator

def Regression():
    estimator = LogisticRegression(solver='saga')
    return estimator

def MLP():
    estimator = MLPClassifier(hidden_layer_sizes=(64,60,58),
                              activation='logistic',
                              max_iter= 500)
    return estimator

def KNN():
    estimator = KNeighborsClassifier(n_neighbors=1,weights='distance')
    return estimator

def Forest():
    estimator = RandomForestClassifier(n_estimators=10, criterion='entropy')
    return estimator

def XGBoost():
    estimator = XGBClassifier(n_estimators=10,objective='binary:logistic')
    return estimator

def SVM():
    estimator = SVC(kernel='linear',C = 100,gamma=100)
    return estimator

switcher = {
        'regression': Regression(),
        'mlp': MLP(),
        'knn': KNN(),
        'forest': Forest(),
        'svm': SVM(),
        'xgboost': XGBoost()
        }