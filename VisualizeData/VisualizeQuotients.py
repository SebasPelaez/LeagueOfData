import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D

def StochasticNeighborEmbedding(X,Y,dimension):
    tsne = TSNE(n_components=dimension,perplexity=40,learning_rate=300,n_iter=5000,
                    verbose=1)
    X_embedded = tsne.fit_transform(X)
    if dimension == 2:
        scatter2D(X_embedded, Y)   
        plt.savefig('Images/quotients_tsne-2D.png', dpi=120)
    else:
        scatter3D(X_embedded, Y)   
        plt.savefig('Images/quotients_tsne-3D.png', dpi=120)
    
def PrincipalComponents(X,Y,dimension):
    pca = PCA(n_components=dimension)
    X_embedded = pca.fit_transform(X)
    if dimension == 2:        
        scatter2D(X_embedded, Y)
        plt.savefig('Images/quotients_pca-2D.png', dpi=120)
    else:
        scatter3D(X_embedded, Y)
        plt.savefig('Images/quotients_pca-3D.png', dpi=120)
       
    
#https://github.com/oreillymedia/t-SNE-tutorial
def scatter2D(x, y):
    
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111,aspect='equal')
    
    colors = ['navy', 'turquoise']
    target_names = ['Lose (0)','Win (1)']
    lw = 2
    
    for color, i, target_name in zip(colors, [0, 1], target_names):
        ax.scatter(x[y == i, 0], x[y == i, 1], color=color, 
                    alpha=.8, lw=lw,label=target_name)
    plt.legend(loc='best', shadow=False, scatterpoints=1)
    plt.title('Quotients 2D')

    # We add the labels for each digit.
    txts = []
    for i in range(2):
        # Position of each label.
        xtext, ytext = np.median(x[y == i, :], axis=0)
        txt = ax.text(xtext, ytext, str(i), fontsize=24)
        txt.set_path_effects([
            PathEffects.Stroke(linewidth=5, foreground="w"),
            PathEffects.Normal()])
        txts.append(txt)

def scatter3D(X_embedded, Y):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    colors = ['navy', 'turquoise']
    target_names = ['Lose (0)','Win (1)']
    lw = 2
    
    for color, i, target_name in zip(colors, [0, 1], target_names):
        ax.scatter(X_embedded[Y == i, 0], X_embedded[Y == i, 1],X_embedded[Y == i, 2], color=color, 
                    alpha=.8, lw=lw,label=target_name)
    plt.legend(loc='best', shadow=False, scatterpoints=1)
    plt.title('Quotients 3D')