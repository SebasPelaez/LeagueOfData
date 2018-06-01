import numpy as np

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def KNN(X,Y):
    folds = 100
    neighbors = 5
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
    
      estimator = KNeighborsClassifier(n_neighbors=neighbors,weights='distance')
      estimator.fit(X_train, y_train)
          
      # Predecir los resultados de prueba
      y_pred = estimator.predict(X_test)
      
      cm = confusion_matrix(y_test, y_pred)
      
      sensibility.append(cm[0,0]/(cm[0,0]+cm[1,0]))
      specificity.append(cm[1,1]/(cm[1,1]+cm[0,1]))
      accuracy.append((cm[0,0]+cm[1,1])/np.sum(cm))
      precision.append(cm[0,0]/(cm[0,0]+cm[0,1]))
       
    sensibility = np.mean(sensibility)
    specificity = np.mean(specificity)
    accuracy = np.mean(accuracy)
    error = 1 - accuracy
    precision = np.mean(precision)
    results = [sensibility,specificity,accuracy,error,precision]
    
    return results