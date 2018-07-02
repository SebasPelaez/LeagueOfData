from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from mlxtend.plotting import plot_sequential_feature_selection as plot_sfs
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

from Models.EstimatorSelector import Selector

def FeatureSelector(X,Y,estimator):
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
    
    model = Selector(estimator)
    
    sfs = SFS(estimator=model, 
               k_features=(3, 32),
               forward=True, 
               floating=False, 
               scoring='accuracy',
               cv=5)
    
    pipe = make_pipeline(StandardScaler(), sfs)
    
    pipe.fit(X_train, y_train)
    
    print('Best combination (Accuracy: %.3f): %s\n' % (sfs.k_score_, sfs.k_feature_idx_))
    plot_sfs(sfs.get_metric_dict(), kind='std_err');
    
    return sfs.k_feature_idx_

def FeatureExtraction(X):
    pca = PCA(n_components=5)
    X_pca = pca.fit_transform(X)
    return X_pca 