import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from InfoExtract import ExtractData

data_columns = ['matches_played','percentage_blue_win','percentage_red_win',
                'mean_blue_win_time','mean_red_win_time','mean_win_time',
                'mean_kills','mean_deaths','mean_assis','percentage_fb','mean_fb_time',
                'mean_nofb_time','percentage_ft','mean_ft_time','mean_noft_time',
                'mean_total_towers','percentage_fthreetowers','percentage_fdragon','mean_fdragon_time',
                'mean_dragons','percentage_herald','mean_herald_time','mean_barons',
                'mean_fbaron_time','percentage_fbaron','mean_totalgold','mean_golddiff_at10',
                'mean_golddiff_at15','mean_experience_at10','mean_wards','mean_wards_kill','mean_creeps_kill']

full_data = pd.read_csv('./data/OraclesElixir/FullData.csv')
teams = pd.DataFrame(columns = data_columns)

team_a = full_data[full_data['team']=='SK Telecom T1']

k = 0
for i in range(5,len(team_a)):
    data = ExtractData(team_a.iloc[0:i,:])
    teams.loc[k] = data
    k = k + 1