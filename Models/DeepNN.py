from keras.models import Sequential
from keras.layers import Dense

from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np

def deepNN(X,Y):
    folds = 10
    sensibility = []
    specificity = []
    accuracy = []
    precision = []
    
    #Create model
    model = Sequential()
    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    model.add(Dense(32, input_dim=32, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(28, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(24, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(20, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(16, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(12, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(8, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(4, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(1, kernel_initializer='uniform', activation='sigmoid'))
    
    for i in range(0,folds):
      X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
      
      #Normalización de los datos
      sc_X = StandardScaler()
      X_train = sc_X.fit_transform(X_train)
      X_test = sc_X.transform(X_test)
    
      # Fit the model
      model.fit(X_train, y_train, epochs=150, batch_size=10,verbose=0)
      
      # calculate predictions
      y_pred = model.predict(X_test)
      y_pred = [round(x[0]) for x in y_pred]
      
      cm = confusion_matrix(y_test, y_pred)
      print(cm)
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
    #scores = model.evaluate(X, Y)
    #print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))    