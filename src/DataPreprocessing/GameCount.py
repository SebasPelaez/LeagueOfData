import numpy as np
import pandas as pd

def addGameCount(full_data):
    teams = np.unique(full_data['team'])
    teams = teams.reshape(len(teams),1)
    teams = np.concatenate((teams,np.zeros((len(teams),1))),axis=1)
    gamecount = np.zeros((len(full_data),1))
    for i in full_data.index:
        team = full_data.loc[i]['team']
        team_index = np.where(teams[:,0]==team)
        gamecount[i] = teams[team_index,1]
        teams[team_index,1] = teams[team_index,1] + 1
    
    full_data.insert(loc=0,column='gamecount',value=gamecount) 
    return full_data