#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 20:05:32 2018

@author: root
"""
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

full_data = pd.read_csv('/home/sebas/Escritorio/LeagueOfData/data/OraclesElixir/FullData.csv')

game_results = full_data.loc[:,('side','result')]
blue_side = game_results[game_results['side']=='Blue']
unique_elements, counts_elements = np.unique(blue_side['result'], return_counts=True)
wins = counts_elements[1]
lose = counts_elements[0]
percentage_wins = "{0:.2f}".format((wins / (wins + lose)) * 100)
percentage_lose = "{0:.2f}".format((lose / (wins + lose)) * 100)
plt.xlabel('Posición en el mapa')
plt.ylabel('Número de Victorias')
plt.title('Victorias vs Lado del Mapa')
plt.bar(0,wins,color = "b", width = 1 , label = percentage_wins+"%")
plt.bar(1,lose,color = "r", width = 1 , label = percentage_lose+"%")
plt.legend()
plt.xticks([0,1],["Lado Azul","Lado Rojo"])
plt.show()

game_results = full_data.loc[:,('result','fb')]
fb_wins = game_results[game_results['result']==1]
unique_elements, counts_elements = np.unique(fb_wins['fb'], return_counts=True)
wins = counts_elements[2]
lose = counts_elements[1]

#Primera sangre
percentage_wins = "{0:.2f}".format((wins / (wins + lose)) * 100)
percentage_lose = "{0:.2f}".format((lose / (wins + lose)) * 100)
plt.xlabel('Primera Sangre')
plt.ylabel('Número de Victorias')
plt.title('Victorias vs Por Primera Sangre')
plt.bar(0,wins,color = "b", width = 1 , label = percentage_wins+"%")
plt.bar(1,lose,color = "r", width = 1 , label = percentage_lose+"%")
plt.legend()
plt.xticks([0,1],["Si","No"])
plt.show()

#Primera Torre
game_results = full_data.loc[:,('result','ft')]
ft_wins = game_results[game_results['result']==1]
unique_elements, counts_elements = np.unique(ft_wins['ft'], return_counts=True)
wins = counts_elements[1]
lose = counts_elements[0]

percentage_wins = "{0:.2f}".format((wins / (wins + lose)) * 100)
percentage_lose = "{0:.2f}".format((lose / (wins + lose)) * 100)
plt.xlabel('Primera Torre')
plt.ylabel('Número de Victorias')
plt.title('Victorias vs Por Primera Torre')
plt.bar(0,wins,color = "b", width = 1 , label = percentage_wins+"%")
plt.bar(1,lose,color = "r", width = 1 , label = percentage_lose+"%")
plt.legend()
plt.xticks([0,1],["Si","No"])
plt.show()

#Primer Dragon
game_results = full_data.loc[:,('result','fd')]
fd_wins = game_results[game_results['result']==1]
unique_elements, counts_elements = np.unique(fd_wins['fd'], return_counts=True)
wins = counts_elements[2]
lose = counts_elements[1]

percentage_wins = "{0:.2f}".format((wins / (wins + lose)) * 100)
percentage_lose = "{0:.2f}".format((lose / (wins + lose)) * 100)
plt.xlabel('Primer Dragón')
plt.ylabel('Número de Victorias')
plt.title('Victorias vs Por Primer Dragón')
plt.bar(0,wins,color = "b", width = 1 , label = percentage_wins+"%")
plt.bar(1,lose,color = "r", width = 1 , label = percentage_lose+"%")
plt.legend()
plt.xticks([0,1],["Si","No"])
plt.show()

#Duración Partidas
game_results = full_data.loc[:,('result','gamelength')]
unique_elements, counts_elements = np.unique(game_results['gamelength'], return_counts=True)
IC = [np.mean(unique_elements)-np.std(unique_elements),np.mean(unique_elements)+np.std(unique_elements)]
b = unique_elements>=IC[0]
a = unique_elements[b]
c = counts_elements[b]
b = a<=IC[1]
a = a[b]
c = c[b]

plt.plot(a,c, color = 'black', label = 'Duración')
plt.legend()
plt.title('Duración de las partidas')
plt.xlabel('Minutos')
plt.ylabel('Número de partidas')
plt.show()

#VICTORIA POR DIFERENCIA DE MUERTE
game_results = full_data.loc[:,('side','result','teamkills')]
blue = game_results[game_results['side']=='Blue']
red = game_results[game_results['side']=='Red']
blue = blue['teamkills'].values
red = red['teamkills'].values
difference = blue - red
unique_elements, counts_elements = np.unique(difference, return_counts=True)
plt.plot(unique_elements,counts_elements, color = 'black', label = 'Duración')
plt.legend()
plt.title('Duración de las partidas')
plt.xlabel('Minutos')
plt.ylabel('Número de partidas')
plt.show()

plt.xlabel('Diferencia de Muertes')
plt.ylabel('Número de Partidas')
plt.title('Diferencia de Muertes por Partida')
n = np.arange(len(unique_elements))
for i in n:
    plt.bar(i,counts_elements[i],color = "b", width = 0.4)
plt.xticks(n,unique_elements)
plt.show()

#DIFERENCIA DE ORO
game_results = full_data.loc[:,('result','gdat10','gdat15')]
gold_wins = game_results[game_results['result']==1]

wins_positive_gold = len(gold_wins[gold_wins['gdat10'] >= 0])
wins_negative_gold = len(gold_wins) - wins_positive_gold
labels = 'Diferencia de Oro Positiva','Diferencia de Oro Negativa'
wins = [wins_positive_gold,wins_negative_gold]
plt.pie(wins, labels=labels, autopct='%1.1f%%', shadow=True)
plt.title('Victorias con diferencia de Oro al Minuto 10')
plt.show()

wins_positive_gold = len(gold_wins[gold_wins['gdat15'] >= 0])
wins_negative_gold = len(gold_wins) - wins_positive_gold
labels = 'Diferencia de Oro Positiva','Diferencia de Oro Negativa'
wins = [wins_positive_gold,wins_negative_gold]
plt.pie(wins, labels=labels, autopct='%1.1f%%', shadow=True)
plt.title('Victorias con diferencia de Oro al Minuto 15')
plt.show()

#WARDS
game_results = full_data.loc[:,('result','wards','wardkills','gamelength')]
wins = game_results[game_results['result']==1]
wards = wins['wards'].values
wardkills = wins['wardkills'].values
time = wins['gamelength'].values

fig, axes = plt.subplots(nrows=2, ncols=1)
plt.subplot(211)
plt.scatter(wards,wardkills, color = 'maroon')
plt.xlabel('Wards Puestas')
plt.ylabel('Wards Limpiadas')
plt.title('Creación Vs Limpieza de Wards')

plt.subplot(212)
wards = wards[:] / time[:]
wardkills = wardkills[:] / time[:]
plt.scatter(wards,wardkills, color = 'cyan')
plt.xlabel('Wards Puestas')
plt.ylabel('Wards Limpiadas')
plt.title('Creación Vs Limpieza de Wards (Normalizada)')

plt.tight_layout() 
plt.show()

#Primera sangre y lados
game_results = full_data.loc[:,('result','fb','side')]

#Separo en lado azul y rojo
blue = game_results[game_results['side']=='Blue']
red = game_results[game_results['side']=='Red']

#Separo la Primera Sangre
blue_fb = blue[blue['fb'] == '1']
red_fb = red[red['fb'] == '1']

#Objeto que me permitirá ordenar las gráficas
fig, axes = plt.subplots(nrows=2, ncols=1)

#Gráfica 1
plt.subplot(211)
#Cuento cuantas victorias y derrotas hay en el subconjunto
unique_elements, counts_elements = np.unique(blue_fb['result'], return_counts=True)
wins = counts_elements[1]
lose = counts_elements[0]
percentage_wins = "{0:.2f}".format((wins / (wins + lose)) * 100)
percentage_lose = "{0:.2f}".format((lose / (wins + lose)) * 100)

plt.bar(0,wins,color = "b", width = 1 , label = percentage_wins+"%")
plt.bar(1,lose,color = "r", width = 1 , label = percentage_lose+"%")
plt.legend()
plt.xticks([0,1],["Si","No"])
plt.xlabel('Victoria')
plt.ylabel('# Partidas')
plt.title('Lado Azul y Primera Sangre')

#Gráfica 2
plt.subplot(212)
#Cuento cuantas victorias y derrotas hay en el subconjunto
unique_elements, counts_elements = np.unique(red_fb['result'], return_counts=True)
wins = counts_elements[1]
lose = counts_elements[0]
percentage_wins = "{0:.2f}".format((wins / (wins + lose)) * 100)
percentage_lose = "{0:.2f}".format((lose / (wins + lose)) * 100)

plt.bar(0,wins,color = "b", width = 1 , label = percentage_wins+"%")
plt.bar(1,lose,color = "r", width = 1 , label = percentage_lose+"%")
plt.legend()
plt.xticks([0,1],["Si","No"])
plt.xlabel('Victoria')
plt.ylabel('# Partidas')
plt.title('Lado Rojo y Primera Sangre')

plt.tight_layout() 
plt.show()

#Primera sangre y lados y primera torre
game_results = full_data.loc[:,('result','fb','side','ft')]

#Separo en lado azul y rojo
blue = game_results[game_results['side']=='Blue']
red = game_results[game_results['side']=='Red']

#Separo en primera torre
blue_ft = blue[blue['ft']==1]
red_ft = red[red['ft']==1]

#Separo la Primera Sangre
blue_fb = blue_ft[blue_ft['fb'] == '1']
red_fb = red_ft[red_ft['fb'] == '1']

#Gráfica 1
plt.figure(1)
#Cuento cuantas victorias y derrotas hay en el subconjunto
unique_elements, counts_elements = np.unique(blue_fb['result'], return_counts=True)
wins = counts_elements[1]
lose = counts_elements[0]
percentage_wins = "{0:.2f}".format((wins / (wins + lose)) * 100)
percentage_lose = "{0:.2f}".format((lose / (wins + lose)) * 100)

plt.bar(0,wins,color = "orangered", width = 1 , label = percentage_wins+"%")
plt.bar(1,lose,color = "steelblue", width = 1 , label = percentage_lose+"%")
plt.legend()
plt.xticks([0,1],["Si","No"])
plt.xlabel('Victoria')
plt.ylabel('# Partidas')
plt.title('Lado Azul, Primera Sangre y Primera Torre')
plt.text(0.9, 1100, '# Partidas: '+str(wins + lose), style='italic',
        bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})

#Gráfica 2
plt.figure(2)
#Cuento cuantas victorias y derrotas hay en el subconjunto
unique_elements, counts_elements = np.unique(red_fb['result'], return_counts=True)
wins = counts_elements[1]
lose = counts_elements[0]
percentage_wins = "{0:.2f}".format((wins / (wins + lose)) * 100)
percentage_lose = "{0:.2f}".format((lose / (wins + lose)) * 100)

plt.bar(0,wins,color = "orangered", width = 1 , label = percentage_wins+"%")
plt.bar(1,lose,color = "steelblue", width = 1 , label = percentage_lose+"%")
plt.legend()
plt.xticks([0,1],["Si","No"])
plt.xlabel('Victoria')
plt.ylabel('# Partidas')
plt.title('Lado Rojo, Primera Sangre y Primera Torre')
plt.text(0.9, 700, '# Partidas: '+str(wins + lose), style='italic',
        bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})

plt.show()