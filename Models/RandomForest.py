import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def RandomForest(X,Y):
    folds = 100
    n_trees = 100
    relevant_features = []
    accuracy = []
    for i in range(0,folds):
      X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
      
      #Normalización de los datos
      sc_X = StandardScaler()
      X_train = sc_X.fit_transform(X_train)
      X_test = sc_X.transform(X_test)
    
      regressor = RandomForestClassifier(n_estimators=n_trees, criterion='entropy')
      regressor.fit(X_train, y_train)
      
      relevant_features.append(regressor.feature_importances_)
    
      # Predecir los resultados de prueba
      y_pred = regressor.predict(X_test)
      
      cm = confusion_matrix(y_test, y_pred)
      accuracy.append((cm[0,0]+cm[1,1])/(cm[0,0]+cm[0,1]+cm[1,0]+cm[1,1]))
       
    relevant_features = np.asmatrix(relevant_features)
    print (np.mean(relevant_features,axis = 0))
    print (np.mean(accuracy))