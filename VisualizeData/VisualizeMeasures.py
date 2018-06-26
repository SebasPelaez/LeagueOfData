import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import auc

def plot_ROC(tprs,mean_fpr,aucs):
    mean_tpr = np.mean(tprs, axis=0)
    mean_tpr[-1] = 1.0
    mean_auc = auc(mean_fpr, mean_tpr)
    std_auc = np.std(aucs)
    plt.subplots(figsize=(8,8))
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

def plot_measures(sensibility,specificity,accuracy,precision):
    
    sensibility = np.around(sensibility,decimals=5)
    specificity = np.around(specificity,decimals=5)
    accuracy = np.around(accuracy,decimals=5)
    precision = np.around(precision,decimals=5)
        
    means = (np.mean(sensibility),np.mean(specificity),np.mean(accuracy),
            np.mean(precision))
    stds = (np.std(sensibility),np.std(specificity),np.std(accuracy),
            np.std(precision))
    maxs = (np.max(sensibility),np.max(specificity),np.max(accuracy),
            np.max(precision))
        
    ind = np.arange(len(means))  # the x locations for the groups
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots(figsize=(8,8))
    rects1 = ax.bar(ind - width/2, means, width, yerr=stds,
                    color='SkyBlue', label='Mean')
    rects2 = ax.bar(ind + width/2, maxs, width, color='IndianRed', 
                    label='Maximum')
    
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Percentage')
    ax.set_title('Measures of error')
    ax.set_xticks(ind)
    ax.set_xticklabels(('Sensibility', 'Specificity', 'Accuracy', 'Precision'))
    ax.legend()
    
    autolabel(rects1,ax, "left")
    autolabel(rects2,ax, "right")
    
    plt.show()
    
def autolabel(rects, ax,xpos='center'):
    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{0:.2f}'.format(height), ha=ha[xpos], va='bottom')    