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