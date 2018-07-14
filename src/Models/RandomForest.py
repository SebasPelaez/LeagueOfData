from Models.Classifier import Classify
from Models.EstimatorSelector import Selector

def RandomForest(X,Y,estimator):
    model = Selector(estimator)
    results = Classify(X,Y,model)
    
    return results