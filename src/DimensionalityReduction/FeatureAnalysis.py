import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

def Pearson(X,Y):
    pearson_coef = np.corrcoef(X,Y,rowvar=False)
    
    plt.subplots(figsize=(15,12))
    ax1 = sns.heatmap(pearson_coef,cmap=plt.cm.jet,annot=False)    
    
def Fisher(X,Y,data_columns):
    ind_lose = Y == 0
    ind_win = Y == 1
    
    mean_lose = np.mean(X[ind_lose,:],axis=0).reshape((1,32))
    mean_win = np.mean(X[ind_win,:],axis=0).reshape((1,32))  
    mean_tot = np.concatenate((mean_lose,mean_win),axis=0)
    
    std_lose = np.std(X[ind_lose,:],axis=0).reshape((1,32))
    std_win = np.std(X[ind_win,:],axis=0).reshape((1,32))
    std_tot = np.concatenate((std_lose,std_win),axis=0)
    
    coef = np.zeros((1,len(X[0])))
    
    for i in range(0,2):
        for j in range(0,2):
            if (j != i):
                numerador = np.power((mean_tot[i,:] - mean_tot[j,:]),2)
                denominador = std_tot[i,:] + std_tot[j,:]
                coef = coef + (numerador/denominador)
            
    coefN = coef /np.max(coef)
    plt.subplots(figsize=(15,10))
    plt.xlabel('Caracteristicas')
    plt.ylabel('Capacidad Discriminate')
    plt.title('Indice de Fisher Normalizado')
    n = np.arange(32)
    for i in n:
        col = 'blue' if coefN[0,i]>0.4 else 'lightgreen'
        plt.bar(i,coefN[0,i],color=col)
    plt.xticks(n,data_columns,rotation=90)
    plt.plot([0, 32], [0.4, 0.4], color='red', linestyle='-', linewidth=3)
    plt.show()
        
def ReductionAnalysis(X,Y,sw):
    components = 32
    if sw == 'pca':
        reduction = PCA(n_components=components)
        X = reduction.fit_transform(X)
    else:
        if sw == 'lda':
            reduction = LinearDiscriminantAnalysis(n_components=components)
            X = reduction.fit_transform(X,Y)
    variance = np.zeros(components)
    k = 0
    c_max = -1
    for i in reduction.explained_variance_ratio_:
        if k == 0 :
            variance[k] = i
        else:
            variance[k] = variance[k-1] + i
        if(variance[k]>0.99 and c_max==-1):
            c_max = k
        k = k + 1
        
    plt.subplots(figsize=(10,8))
    plt.xlabel('Components')
    plt.ylabel('Explained Variance')
    plt.title('Component Analysis')
    plt.plot(variance)
    plt.plot([c_max, c_max], [0.3,1], color='red', linestyle=':', linewidth=2)
