
import numpy as np
import pandas as pd

def fix_week_time_series(csv):
    df = pd.read_csv("..\data\()".format(csv))
    df['index'] = df['index'].str.replace(" W", "-")
    df['index'] = pd.to_datetime(df['index'].add('-0'), format='%Y-%W-%w')
    return df
