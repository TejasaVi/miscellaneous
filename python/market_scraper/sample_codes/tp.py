from time import sleep
from datetime import datetime,date
import sqlite3 as sql
import pandas as pd

open_price = 17464
open_io = 6731 + 6256


def latest_change():
    data = pd.read_sql('SELECT * FROM nifty_modified ORDER  BY time DESC NULLS LAST LIMIT 11;', conn)
    return data


conn = sql.connect('test.db')
data = pd.read_sql('SELECT * FROM nifty', conn)
data = data.sort_values(['strikePrice_callopt','time'])
data['status'] = 'NA'
for index, row in data.iterrows():
    # Increase in Price and IO
    if row['underlyingValue_putopt'] > open_price and row['openInterest_callopt'] > open_io:
        data.at[index,'status'] = 'Long Buildup'
    elif row['underlyingValue_putopt'] > open_price and row['openInterest_callopt'] < open_io:
        data.at[index,'status'] = 'Short Covering'
    elif row['underlyingValue_putopt'] < open_price and row['openInterest_callopt'] < open_io:
        data.at[index,'status'] = 'Short Buildup'
    else:
        data.at[index,'status'] = 'Long unwinding'
data.to_sql('nifty_modified', conn,if_exists='append')
print(latest_change())

