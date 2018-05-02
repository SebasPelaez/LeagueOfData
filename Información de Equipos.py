import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

full_data = pd.read_csv('./data/OraclesElixir/FullData.csv')

teams = np.unique(full_data['team'])
teams = np.reshape(teams,(len(teams),1))

team_a = full_data[full_data['team']=='SK Telecom T1']

#Partidos Jugados
matches_played = len(team_a)

#Porcentaje victorias lado Azul
blue_side = team_a[team_a['side']=='Blue']
unique_elements, counts_elements = np.unique(blue_side['result'], return_counts=True)
wins = counts_elements[1]
lose = counts_elements[0]
percentage_wins_blue_side = "{0:.2f}".format((wins / (wins + lose)) * 100)

#Porcentaje victorias lado Rojo
red_side = team_a[team_a['side']=='Red']
unique_elements, counts_elements = np.unique(red_side['result'], return_counts=True)
wins = counts_elements[1]
lose = counts_elements[0]
percentage_wins_red_side = "{0:.2f}".format((wins / (wins + lose)) * 100)

#Promedio tiempo de victoria
side = team_a[team_a['side']=='Blue']
mean_win = side[side['result']==1]
blue_mean_time_win = np.mean(mean_win['gamelength'])

side = team_a[team_a['side']=='Red']
mean_win = side[side['result']==1]
red_mean_time_win = np.mean(mean_win['gamelength'])

total_mean_time_win = (blue_mean_time_win + red_mean_time_win)/2

#Promedio KDA
K = np.mean(team_a['k'])
D = np.mean(team_a['d'])
A = np.mean(team_a['a'])

#Primeras Sangre
fb = np.asarray(team_a['fb'], dtype=int)
percentage_fb = (np.sum(fb) * 100)/matches_played
fb = team_a[team_a['fb']=='1']
nofb = team_a[team_a['fb']=='0']
mean_fb_time = np.mean(np.asarray(fb['fbtime'], dtype=float)) 
mean_nofb_time = np.mean(np.asarray(nofb['fbtime'], dtype=float)) 

#TORRES
percentage_ftw = (np.sum(team_a['ft']) * 100)/matches_played
tw = team_a[team_a['ft']==1]
notw = team_a[team_a['ft']==0]
mean_ftw_time = np.mean(np.asarray(fb['fttime'], dtype=float)) 
mean_noftw_time = np.mean(np.asarray(nofb['fttime'], dtype=float))

total_tower = np.mean(team_a['teamtowerkills'])
total_tower = np.around(total_tower)
percentage_fthreetw = (np.sum(team_a['firsttothreetowers']) * 100)/matches_played

#DRAGONES
fd = np.asarray(team_a['fd'], dtype=int)
percentage_fdragon = (np.sum(fd) * 100)/matches_played
fd = team_a[team_a['fd']==1]
mean_fd_time = np.mean(np.asarray(fb['fdtime'].dropna(how='any'), dtype=float)) 
total_dragon = np.mean(team_a['teamdragkills'])
total_dragon = np.around(total_dragon)

#HERALDOS
without_nan = team_a['herald'].dropna(how='any')
percentage_herald = (np.sum(without_nan) * 100)/len(without_nan)

herald = team_a[team_a['herald']==1]
mean_herald_time = np.mean(np.asarray(herald['heraldtime'].dropna(how='any'), dtype=float)) 

#BARONES
fbaron = np.asarray(team_a['fbaron'], dtype=int)
percentage_fbaron = (np.sum(fbaron) * 100)/matches_played
fbaron = team_a[team_a['fbaron']==1]
mean_fbaron_time = np.mean(np.asarray(fb['fbarontime'].dropna(how='any'), dtype=float)) 
total_baron = np.mean(team_a['teambaronkills'])
total_baron = np.around(total_baron)

#ORO
mean_gold = np.mean(team_a['totalgold'] / team_a['gamelength'])
mean_gold_difference_at10 = np.mean(team_a['gdat10'])
mean_gold_difference_at15 = np.mean(team_a['gdat15'])

#EXPERIENCIA
mean_experience_difference_at10 = np.mean(team_a['xpdat10'])

#WARDS
mean_wards = np.mean(team_a['wards']/ team_a['gamelength'])
mean_wards_kill = np.mean(team_a['wardkills'] / team_a['gamelength'])

#MINIONS AND NEUTRAL MOSTERS
mean_creeps_kill = np.mean((team_a['minionkills']+team_a['monsterkills'])/ team_a['gamelength'])
