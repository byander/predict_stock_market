import pandas as pd
from db import connect

def get_dataset():
    con = connect()
    sql = '''SELECT symbol, date, open, high, low, close, volume FROM time_series_daily WHERE date >= '2018-01-01' ORDER BY date;'''
    # sql = '''SELECT symbol, date, open, high, low, close, volume FROM time_series_daily WHERE date < '2018-01-01' ORDER BY date;'''
    ds = pd.read_sql_query(sql, con)
    con.close()

    return ds

def get_data_close_last_30():
    con = connect()
    sql = '''SELECT symbol, date, open, high, low, close, volume FROM time_series_daily WHERE date >= '2018-01-01' ORDER BY date;'''

    ds = pd.read_sql_query(sql, con)
    con.close()

    ds['day'] =  pd.to_datetime(ds['date']).dt.day

    print(ds[:8])

    return ds