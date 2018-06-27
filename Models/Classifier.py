import numpy as np

from scipy import interp
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc

from VisualizeData.VisualizeMeasures import plot_measures,plot_ROC

def Classify(X,Y,estimator):
    folds = 100
    sensibility = []
    specificity = []
    accuracy = []
    precision = []
    
    tprs = []
    aucs = []
    mean_fpr = np.linspace(0, 1, 100)
    y_proba = []
    
    for i in range(0,folds):
      X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
      print(i)
      #Normalización de los datos
      sc_X = StandardScaler()
      X_train = sc_X.fit_transform(X_train)
      X_test = sc_X.transform(X_test)
    
      estimator.fit(X_train, y_train)
          
      # Predecir los resultados de prueba
      y_pred = estimator.predict(X_test)
      y_proba = estimator.predict_proba(X_test)
      cm = confusion_matrix(y_test, y_pred)
      
      # Compute ROC curve and area the curve
      fpr, tpr, thresholds = roc_curve(y_test, y_proba[:, 1])
      tprs.append(interp(mean_fpr, fpr, tpr))
      tprs[-1][0] = 0.0
      roc_auc = auc(fpr, tpr)
      aucs.append(roc_auc)
     
      sensibility.append(cm[1,1]/(cm[1,1]+cm[1,0]))
      specificity.append(cm[0,0]/(cm[0,0]+cm[0,1]))
      accuracy.append((cm[0,0]+cm[1,1])/np.sum(cm))      
      precision.append(cm[1,1]/(cm[1,1]+cm[0,1]))
    
    plot_ROC(tprs,mean_fpr,aucs)
    plot_measures(sensibility,specificity,accuracy,precision)
    
    sensibility = '{}+-{}'.format(np.around(np.mean(sensibility),decimals=3),np.around(np.std(sensibility),decimals=3))
    specificity = '{}+-{}'.format(np.around(np.mean(specificity),decimals=3),np.around(np.std(specificity),decimals=3))
    error = 1 - np.around(np.mean(accuracy),decimals=5)
    accuracy = '{}+-{}'.format(np.around(np.mean(accuracy),decimals=3),np.around(np.std(accuracy),decimals=3))
    precision = '{}+-{}'.format(np.around(np.mean(precision),decimals=3),np.around(np.std(precision),decimals=3))
    results = [sensibility,specificity,accuracy,error,precision]
    
    return results