import numpy as np
import pandas as pd
import datetime

def fix_week_time_series(csv):
    df = pd.read_csv("..\data\()".format(csv))
    df['index'] = df['index'].str.replace(" W", "-")
    df['index'] = pd.to_datetime(df['index'].add('-0'), format='%Y-%W-%w')
    return df


def make_ts(start_date, periods, freq='YS'):
    '''
    Make a random timeseries dataset to play with. Currently only yearly data.
    start_date = Year
    periods = number of data points
    frequency = Number of of observations before the seasonal pattern repeats. Default is YS.
    '''


    y = pd.Series(pd.date_range(start_date, periods=periods, freq=freq))
    z = pd.Series(np.random.random((y.shape[0],))*100)
    y = pd.concat([y, z], axis=1)
    y.columns = ['Year', 'Observation']
    y.set_index('Year', inplace = True)
    return y