import numpy as np
import pandas as pd

def Quotient(full_data,teams,full_results,data_columns):
    quotients = pd.DataFrame(columns = data_columns)
    k = 0
    for i in range(0,1000,2):
        team_b = full_data.loc[i]
        team_r = full_data.loc[i+1]
        if(np.isin(team_b['team'],teams) and  np.isin(team_r['team'],teams)):
            result = 1 if team_b['result'] == 1 else 0
            game_b = team_b['gamecount'] - 5
            game_r = team_r['gamecount'] - 5
            if(game_b  < 1):
                game_b = 0
            if(game_r  < 1):
                game_r = 0
            blue_index = np.where(teams[:]==team_b['team'])[0][0]
            red_index = np.where(teams[:]==team_r['team'])[0][0]
            if(blue_index<len(full_results) and red_index<len(full_results)):
                results_blue = full_results[blue_index].loc[game_b]
                results_red = full_results[red_index].loc[game_r]
                cociente = results_blue/results_red
                cociente['result'] = result
                FixQuotient(cociente)
                quotients.loc[k] = cociente
                k = k + 1
            else:
                print("Equipo con pocos partidos para ser evaluado")
        else:
            print("No existe alguno de loso equipos")
    return quotients
            
def FixQuotient(cociente):
    cociente['percentage_blue_win'] = ValidateQuotient(cociente['percentage_blue_win'],1)
    cociente['percentage_red_win'] = ValidateQuotient(cociente['percentage_red_win'],1)
    cociente['mean_blue_win_time'] = ValidateQuotient(cociente['mean_blue_win_time'],0)
    cociente['mean_red_win_time'] = ValidateQuotient(cociente['mean_red_win_time'],0)
    cociente['mean_win_time'] = ValidateQuotient(cociente['mean_win_time'],0)
    cociente['percentage_fb'] = ValidateQuotient(cociente['percentage_fb'],1)
    cociente['mean_fb_time'] = ValidateQuotient(cociente['mean_fb_time'],0)
    cociente['mean_nofb_time'] = ValidateQuotient(cociente['mean_nofb_time'],0)
    cociente['percentage_ft'] = ValidateQuotient(cociente['percentage_ft'],1)
    cociente['mean_ft_time'] = ValidateQuotient(cociente['mean_ft_time'],0)
    cociente['mean_noft_time'] = ValidateQuotient(cociente['mean_noft_time'],0)
    cociente['percentage_fthreetowers'] = ValidateQuotient(cociente['percentage_fthreetowers'],1)
    cociente['percentage_fdragon'] = ValidateQuotient(cociente['percentage_fdragon'],1)
    cociente['mean_fdragon_time'] = ValidateQuotient(cociente['mean_fdragon_time'],0)
    cociente['mean_dragons'] = ValidateQuotient(cociente['mean_dragons'],1)
    cociente['percentage_herald'] = ValidateQuotient(cociente['percentage_herald'],1)
    cociente['mean_herald_time'] = ValidateQuotient(cociente['mean_herald_time'],0)
    cociente['mean_barons'] = ValidateQuotient(cociente['mean_barons'],1)
    cociente['mean_fbaron_time'] = ValidateQuotient(cociente['mean_fbaron_time'],0)
    cociente['percentage_fbaron'] = ValidateQuotient(cociente['percentage_fbaron'],1)

"""
Esta función lo que nos permite hacer es corregir cuando un cociente es Nan o
inf. Para estos casos existen las siguientes reglas.
En caso tal de que de Nan significa que ambos valores (divisor y dividendo) son 
cero, en cuyo caso nos expresa que ambos equipos estan empatados y por eso se pone
un Uno (1).
En caso de que sea Inf quiere decir que el dividendo es cero lo cual tiene dos
explicaciones.
Primera: El equipo azul (divisor) tiene mas objetivos, por tanto el cociente
debe ser > que 1.
Segunda: El equipo azul ejecuto todo en menos tiempo, por tanto el cociente 
debe ser < que 1.
"""
def ValidateQuotient(quotient,sw):
    if(np.isnan(quotient)):
        quotient = 1
    if(np.isinf(quotient)):
        if(sw == 0):
            quotient = 0.9
        else:
            quotient = 1.1
    return quotient    