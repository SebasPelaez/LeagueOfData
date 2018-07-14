from sklearn.preprocessing import PolynomialFeatures

from Models.Classifier import Classify
from Models.EstimatorSelector import Selector

def LinearModel(X,Y,estimator):
    poly = PolynomialFeatures(degree=1)
    X = poly.fit_transform(X)
    
    model = Selector(estimator)
    results = Classify(X,Y,model)
    
    return results