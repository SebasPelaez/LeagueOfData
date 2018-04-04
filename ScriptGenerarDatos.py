# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

full_data = pd.read_csv('/home/sebas/Escritorio/LeagueofData/data/LeagueofLegends.csv')
game_results = full_data.loc[:,'bResult']
ind_blue_wins = game_results[game_results==1]
ind_red_wins = game_results[game_results==0]

##PARTIDAS GANADAS POR EL LADO AZUL Y PARTIDAS GANADAS POR LE LADO ROJO
wins = ind_blue_wins.size
lose = ind_red_wins.size
plt.xlabel('Posición en el mapa')
plt.ylabel('Número de Victorias')
plt.title('Victorias vs Lado del Mapa')
plt.bar(0,wins,color = "b", width = 1)
plt.bar(1,lose,color = "r", width = 1)
plt.xticks([0,1],["Lado Azul","Lado Rojo"])
plt.legend([wins, lose],["S", "B"])
plt.show()

##PARTIDAS GANADAS POR OBTENER LA PRIMER SANGRE
import ast #Este import me permitirá convertir String en List
kills = full_data.loc[:,('bKills','rKills')]
blue_kills = []
red_kills = []
for i in range(0,len(kills)):
    x = kills['bKills'][i]
    y = kills['rKills'][i]
    blue_kills.append(ast.literal_eval(x))
    red_kills.append(ast.literal_eval(y))
first_blood = []
for i in range(0,7620):
    if len(blue_kills[i]) == 0:
        first_blood.append(0)
    else:
        if len(red_kills[i]) == 0:
            first_blood.append(1)
        else:
            first_blood.append(0 if (blue_kills[i][0][0]>red_kills[i][0][0]) else 1)

fblood_wins = len(game_results[game_results==first_blood[:]])
nfblood_wins = len(game_results[game_results!=first_blood[:]])
plt.xlabel('Primera Sangre')
plt.ylabel('Número de Victorias')
plt.title('Victorias con Primera Sangre')
plt.bar(0,fblood_wins,color = "y", width = 1)
plt.bar(1,nfblood_wins,color = "g", width = 1)
plt.xticks([0,1],["Si","No"])
plt.show()