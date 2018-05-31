import numpy as np
import pandas as pd

from DataPreprocessing.InfoExtract import ExtractData
from DataPreprocessing.ExtractLPL import ExtractLeague
from DataPreprocessing.GameCount import addGameCount
from DataPreprocessing.MakeQuotient import Quotient

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