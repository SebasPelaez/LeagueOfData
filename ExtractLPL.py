import numpy as np
import pandas as pd

def ExtractLeague(full_data):
    leagues = full_data[full_data['league']=='LPL']
    extract_data = full_data.drop(leagues.index[:])
    return extract_data
    