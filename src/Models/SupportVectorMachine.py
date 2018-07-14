from Models.EstimatorSelector import Selector
from Models.Classifier import Classify

def SVM(X,Y,estimator):
    model = Selector(estimator)
    results = Classify(X,Y,model)
    
    return results