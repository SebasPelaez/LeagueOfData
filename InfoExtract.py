import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def ExtractData(team):
    data = []
    #Partidos Jugados
    matches_played = len(team)
            
    #Porcentaje victorias lado Azul
    blue_side = team[team['side']=='Blue']
    unique_elements, counts_elements = np.unique(blue_side['result'], return_counts=True)
    if len(unique_elements) < 2:
        if unique_elements == 1:
            wins = counts_elements[0]
            lose = 0
        else:
            wins = 0
            lose = counts_elements[0]
    else:
        wins = counts_elements[1]
        lose = counts_elements[0]
    percentage_blue_win = "{0:.2f}".format((wins / (wins + lose)) * 100)

    #Porcentaje victorias lado Rojo
    red_side = team[team['side']=='Red']
    unique_elements, counts_elements = np.unique(red_side['result'], return_counts=True)
    if len(unique_elements) < 2:
        if unique_elements == 1:
            wins = counts_elements[0]
            lose = 0
        else:
            wins = 0
            lose = counts_elements[0]
    else:
        wins = counts_elements[1]
        lose = counts_elements[0]
    percentage_red_win = "{0:.2f}".format((wins / (wins + lose)) * 100)
    
    #Promedio tiempo de victoria
    side = team[team['side']=='Blue']
    mean_win = side[side['result']==1]
    if(len(mean_win) == 0):
        mean_blue_win_time = 50
    else:
        mean_blue_win_time = np.mean(mean_win['gamelength'])
    
    side = team[team['side']=='Red']
    mean_win = side[side['result']==1]
    if(len(mean_win) == 0):
        mean_red_win_time = 50
    else:
        mean_red_win_time = np.mean(mean_win['gamelength'])    
    
    mean_win_time = (mean_blue_win_time + mean_red_win_time)/2
    
    #Promedio KDA
    mean_kills = np.mean(team['k'])
    mean_deaths = np.mean(team['d'])
    mean_assis = np.mean(team['a'])
       
    #Primeras Sangre
    fb = np.asarray(team['fb'], dtype=int)
    percentage_fb = (np.sum(fb) * 100)/matches_played
        
    fb = team[team['fb']=='1']
    nofb = team[team['fb']=='0']
    mean_fb_time = np.mean(np.asarray(fb['fbtime'], dtype=float)) 
    mean_nofb_time = np.mean(np.asarray(nofb['fbtime'], dtype=float)) 
    
    #TORRES
    percentage_ft = (np.sum(team['ft']) * 100)/matches_played
    tw = team[team['ft']==1]
    notw = team[team['ft']==0]
    mean_ft_time = np.mean(np.asarray(tw['fttime'], dtype=float)) 
    mean_noft_time = np.mean(np.asarray(notw['fttime'], dtype=float))
    
    mean_total_towers = np.mean(team['teamtowerkills'])
    mean_total_towers = np.around(mean_total_towers)
    percentage_fthreetowers = (np.sum(team['firsttothreetowers']) * 100)/matches_played
        
    #DRAGONES
    fd = np.asarray(team['fd'], dtype=int)
    percentage_fdragon = (np.sum(fd) * 100)/matches_played
    
    fd = team[team['fd']==1]
    mean_fdragon_time = np.mean(np.asarray(fb['fdtime'].dropna(how='any'), dtype=float)) 
    mean_dragons = np.mean(team['teamdragkills'])
    mean_dragons = np.around(mean_dragons)
    
    #HERALDOS
    without_nan = team['herald'].dropna(how='any')
    percentage_herald = (np.sum(without_nan) * 100)/len(without_nan)
    
    herald = team[team['herald']==1]
    mean_herald_time = np.mean(np.asarray(herald['heraldtime'].dropna(how='any'), dtype=float)) 
    
    #BARONES
    fbaron = np.asarray(team['fbaron'], dtype=float)
    percentage_fbaron = (np.sum(fbaron) * 100)/matches_played
    
    fbaron = team[team['fbaron']==1]
    mean_fbaron_time = np.mean(np.asarray(fb['fbarontime'].dropna(how='any'), dtype=float)) 
    mean_barons = np.mean(team['teambaronkills'])
    mean_barons = np.around(mean_barons)
    
    #ORO
    mean_totalgold = np.mean(team['totalgold'] / team['gamelength'])
    mean_golddiff_at10 = np.mean(team['gdat10'])
    mean_golddiff_at15 = np.mean(team['gdat15'])
    
    #EXPERIENCIA
    mean_experience_at10 = np.mean(team['xpdat10'])
    
    #WARDS
    mean_wards = np.mean(team['wards']/ team['gamelength'])
    mean_wards_kill = np.mean(team['wardkills'] / team['gamelength'])
    
    #MINIONS AND NEUTRAL MOSTERS
    mean_creeps_kill = np.mean((team['minionkills']+team['monsterkills'])/ team['gamelength'])
    
    
    data.append(matches_played)
    data.append(percentage_blue_win)
    data.append(percentage_red_win)
    data.append(mean_blue_win_time)
    data.append(mean_red_win_time)
    data.append(mean_win_time)    
    data.append(mean_kills)
    data.append(mean_deaths)
    data.append(mean_assis)    
    data.append(percentage_fb)
    data.append(mean_fb_time)
    data.append(mean_nofb_time)    
    data.append(percentage_ft)
    data.append(mean_ft_time)
    data.append(mean_noft_time)
    data.append(mean_total_towers)
    data.append(percentage_fthreetowers)
    data.append(percentage_fdragon)
    data.append(mean_fdragon_time)
    data.append(mean_dragons)
    data.append(percentage_herald)
    data.append(mean_herald_time)
    data.append(mean_barons)
    data.append(mean_fbaron_time)
    data.append(percentage_fbaron)  
    data.append(mean_totalgold)
    data.append(mean_golddiff_at10)
    data.append(mean_golddiff_at15)
    data.append(mean_experience_at10)
    data.append(mean_wards)
    data.append(mean_wards_kill)
    data.append(mean_creeps_kill)
    
    return data