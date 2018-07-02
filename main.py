import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from DataPreprocessing.InfoExtract import ExtractData
from DataPreprocessing.ExtractLPL import ExtractLeague
from DataPreprocessing.GameCount import addGameCount
from DataPreprocessing.MakeQuotient import Quotient

from VisualizeData.VisualizeQuotients import StochasticNeighborEmbedding,PrincipalComponents

from Models.RandomForest import RandomForest
from Models.KernelDensityEstimator import ParzenWindow
from Models.NearestNeighbors import KNN
from Models.MultilayerPerceptron import MLP
from Models.SupportVectorMachine import SVM
from Models.LinearRegression import LinearModel
from Models.TreeBoosting import TreeBoosting
from Models.DeepNN import deepNN

from DimensionalityReduction.FeatureAnalysis import Pearson, Fisher,ComponentAnalysis
from DimensionalityReduction.FeatureSubset import FeatureSelector,FeatureExtraction

data_columns = ['matches_played','percentage_blue_win','percentage_red_win',
                'mean_blue_win_time','mean_red_win_time','mean_win_time',
                'mean_kills','mean_deaths','mean_assis','percentage_fb','mean_fb_time',
                'mean_nofb_time','percentage_ft','mean_ft_time','mean_noft_time',
                'mean_total_towers','percentage_fthreetowers','percentage_fdragon','mean_fdragon_time',
                'mean_dragons','percentage_herald','mean_herald_time','mean_barons',
                'mean_fbaron_time','percentage_fbaron','mean_totalgold','mean_golddiff_at10',
                'mean_golddiff_at15','mean_experience_at10','mean_wards','mean_wards_kill','mean_creeps_kill',
                'results']

full_data = pd.read_csv('./data/OraclesElixir/FullData.csv')   
    
#Remove LPL League because they don't have full data
extract_data = ExtractLeague(full_data)

#Enumerate the matchs of every team
extract_data = addGameCount(extract_data) 

full_results = []
teams = np.unique(extract_data['team'])

#Generate the team characteristics in every weak, from the fift game.
for j in teams:
    team_data = extract_data[extract_data['team']==j]
    if (len(team_data) >= 5):
        k = 0
        teams_df = pd.DataFrame(columns = data_columns)
        for i in range(5,len(team_data)):
            data = ExtractData(team_data.iloc[0:i,:])
            teams_df.loc[k] = data
            k = k + 1
        full_results.append(teams_df)
    else:
        full_results.append([])
    
#Build the quotient with the team differences
quotients = Quotient(extract_data,teams,full_results,data_columns)

# Execute Forecast
X = quotients.iloc[:,:-1].values
Y = quotients.iloc[:,-1].values

#Visualize Data
StochasticNeighborEmbedding(X,Y,3)
PrincipalComponents(X,Y,3)

# Execute Forecast
results = RandomForest(X,Y,'forest')
results = ParzenWindow(X,Y)
results = KNN(X,Y,'knn')
results = MLP(X,Y,'mlp')
results = SVM(X,Y,'svm')
results = LinearModel(X,Y,'regression')
results = TreeBoosting(X,Y,'xgboost')
results = deepNN(X,Y)

#Feature Analysis
Pearson(X,Y)
Fisher(X,Y,data_columns)

#Feature Selection
FeatureSelector(X,Y,'svm')

X_sel = [0, 1, 2, 4, 6, 10, 11, 12, 15, 16, 17, 18, 22, 23, 24, 25, 26, 27, 29,
         0, 1, 2, 4, 5, 8, 10, 13, 15, 17, 19, 22, 24, 28, 29, 0, 1, 2, 5, 6, 8,
         9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 
         28, 29, 30, 31, 0, 2, 3, 5, 8, 10, 12, 15, 16, 17, 19, 21, 22, 23, 24, 
         25, 26, 27, 28, 30, 2, 3, 11, 12, 14, 15, 18, 19,2, 16, 18, 25,1, 2, 3,
         5, 6, 8, 9, 10, 12, 14, 16, 17, 18, 19, 20, 22, 24, 25, 26, 27, 29
        ]
unique_elements, counts_elements = np.unique(X_sel, return_counts=True)
features = []
plt.subplots(figsize=(12,7))
plt.xlabel('Features')
plt.ylabel('Count')
plt.title('Number of time for Features')
n = np.arange(len(unique_elements))
for i,j in zip(unique_elements, counts_elements):
    plt.bar(i,j)
    features.append(data_columns[i])
plt.xticks(unique_elements,features,rotation=90)
plt.show()

X_sel_idx = [0,1,2,5,8,10,12,15,16,17,18,19,22,24,25,26,27,29]
X_sel_idx = [0,1,2,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,25,26,27,28,29,30,31]
X_sel = X[:,X_sel_idx]

# Execute Forecast
results = RandomForest(X_sel,Y,'forest')
results = ParzenWindow(X_sel,Y)
results = KNN(X_sel,Y,'knn')
results = MLP(X_sel,Y,'mlp')
results = SVM(X_sel,Y,'svm')
results = LinearModel(X_sel,Y,'regression')
results = TreeBoosting(X_sel,Y,'xgboost')
results = deepNN(X_sel,Y)

ComponentAnalysis(X)

X_ext = FeatureExtraction(X)
results = LinearModel(X_ext,Y,'regression')
results = RandomForest(X_ext,Y,'forest')
results = TreeBoosting(X_ext,Y,'xgboost')
results = ParzenWindow(X_ext,Y)
results = KNN(X_ext,Y,'knn')
results = MLP(X_ext,Y,'mlp')
results = deepNN(X_ext,Y)
results = SVM(X_ext,Y,'svm')