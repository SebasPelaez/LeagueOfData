import numpy as np
import matplotlib.pyplot as plt

from scipy import interp
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc

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
    
    mean_tpr = np.mean(tprs, axis=0)
    mean_tpr[-1] = 1.0
    mean_auc = auc(mean_fpr, mean_tpr)
    std_auc = np.std(aucs)
    #plt.subplots(figsize=(8,10))
    plt.plot(mean_fpr, mean_tpr, color='b',
             label=r'Mean ROC (AUC = %0.2f $\pm$ %0.2f)' % (mean_auc, std_auc),
             lw=2, alpha=.8)
    
    std_tpr = np.std(tprs, axis=0)
    tprs_upper = np.minimum(mean_tpr + std_tpr, 1)
    tprs_lower = np.maximum(mean_tpr - std_tpr, 0)
    plt.fill_between(mean_fpr, tprs_lower, tprs_upper, color='grey', alpha=.2,
                     label=r'$\pm$ std. dev.')
    
    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    plt.xlabel('1 - Specificity')
    plt.ylabel('Sensibility')
    plt.title('Curva ROC')
    plt.legend(loc="lower right")
    plt.show()
    
    sensibility = '{}+-{}'.format(np.around(np.mean(sensibility),decimals=3),np.around(np.std(sensibility),decimals=3))
    specificity = '{}+-{}'.format(np.around(np.mean(specificity),decimals=3),np.around(np.std(specificity),decimals=3))
    error = 1 - np.around(np.mean(accuracy),decimals=5)
    accuracy = '{}+-{}'.format(np.around(np.mean(accuracy),decimals=3),np.around(np.std(accuracy),decimals=3))
    precision = '{}+-{}'.format(np.around(np.mean(precision),decimals=3),np.around(np.std(precision),decimals=3))
    results = [sensibility,specificity,accuracy,error,precision]
    
    return results