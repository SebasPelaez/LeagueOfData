import numpy as np
import pandas as pd

def ExtractLeague(full_data):
    leagues = full_data[full_data['league']=='LPL']
    extract_data = full_data.drop(leagues.index[:])
    extract_data = extract_data.reset_index(drop=True)
    return extract_data
    