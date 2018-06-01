import numpy as np

from sklearn.neighbors import KernelDensity
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

def ParzenWindow(X,Y):
    folds = 10
    sensibility = []
    specificity = []
    accuracy = []
    precision = []
    for i in range(0,folds):
        
      X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
      
      ind_win = y_train == 1
      ind_lose = y_train == 0
      X_win = X_train[ind_win,:]
      X_lose = X_train[ind_lose,:]
          
      f_win = estimate(X_win,X_test)
      f_lose = estimate(X_lose,X_test)
      
      f_win = np.reshape(f_win,(len(X_test),1))
      f_lose = np.reshape(f_lose,(len(X_test),1))
      
      f_total = np.concatenate((f_lose,f_win),axis=1)
      y_pred = np.argmax(f_total,axis=1)
      
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

def estimate(X_train,X_test):
    width = 1
    estimator = KernelDensity(bandwidth=width,kernel='gaussian', algorithm='ball_tree')
    estimator.fit(X_train)
    # Predecir los resultados de prueba
    y_pred = estimator.score_samples(X_test)
    return (y_pred)
    
