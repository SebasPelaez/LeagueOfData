import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def Pearson(X,Y):
    pearson_coef = np.corrcoef(X,Y,rowvar=False)
    
    plt.subplots(figsize=(15,10))
    ax1 = sns.heatmap(pearson_coef,cmap=plt.cm.jet,annot=True)    
    
def Fisher(X,Y):
    ind_lose = Y == 0
    ind_win = Y == 1
    
    mean_lose = np.mean(X[ind_lose,:],axis=1)
    mean_win = np.mean(X[ind_win,:],axis=1)    
    mean_tot = np.concatenate((mean_lose,mean_win),axis=1)
    
    std_lose = np.std(X[ind_lose,:],axis=1)
    std_win = np.std(X[ind_win,:],axis=1)
    std_tot = np.concatenate((std_lose,std_win),axis=1)
    
    coef = np.zeros(1,len(X[0]))
    
    for i in range(0,1):
        for j in range(0,1):
            if (j != i):
                numerador = np.power((mean_tot[i,:] - mean_tot[j,:]),2)
                denominador = std_tot[i,:] + std_tot[j,:]
                coef = coef + (numerador/denominador)
            
    coefN = coef /np.max(coef)
    return (coefN)