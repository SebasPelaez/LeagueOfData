import numpy as np

from Models.EstimatorSelector import Selector

from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def SVM(X,Y,estimator):
    folds = 5
    sensibility = []
    specificity = []
    accuracy = []
    precision = []
    for i in range(0,folds):
      
      X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
      
      #Normalización de los datos
      sc_X = StandardScaler()
      X_train = sc_X.fit_transform(X_train)
      X_test = sc_X.transform(X_test)
    
      model = Selector(estimator)
      model.fit(X_train, y_train)
          
      # Predecir los resultados de prueba
      y_pred = model.predict(X_test)
      
      cm = confusion_matrix(y_test, y_pred)
      
      sensibility.append(cm[1,1]/(cm[1,1]+cm[1,0]))
      specificity.append(cm[0,0]/(cm[0,0]+cm[0,1]))
      accuracy.append((cm[0,0]+cm[1,1])/np.sum(cm))      
      precision.append(cm[1,1]/(cm[1,1]+cm[0,1]))
       
    sensibility = '{}+-{}'.format(np.around(np.mean(sensibility),decimals=3),np.around(np.std(sensibility),decimals=3))
    specificity = '{}+-{}'.format(np.around(np.mean(specificity),decimals=3),np.around(np.std(specificity),decimals=3))
    error = 1 - np.around(np.mean(accuracy),decimals=5)
    accuracy = '{}+-{}'.format(np.around(np.mean(accuracy),decimals=3),np.around(np.std(accuracy),decimals=3))
    precision = '{}+-{}'.format(np.around(np.mean(precision),decimals=3),np.around(np.std(precision),decimals=3))
    results = [sensibility,specificity,accuracy,error,precision]
    
    return results