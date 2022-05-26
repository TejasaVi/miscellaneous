import requests
import json
import pandas as pd
import pprint
from time import sleep
from datetime import datetime,date
import sqlite3 as sql
import matplotlib.pyplot as plt

expiry_date = '10-Feb-2022'
symbol = 'NIFTY'
url = 'https://www.nseindia.com/api/option-chain-indices?symbol=' + symbol
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
           'accept-language': 'en,gu;q=0.9,hi;q=0.8',
           'accept-encoding': 'gzip, deflate, br',
           'referer':'https://www.nseindia.com/get-quotes/derivatives?symbol='+ symbol}

def _do_request():
    session = requests.Session()
    request = session.get(url,headers=headers)
    cookies = dict(request.cookies)
    response = session.get(url, headers=headers, cookies=cookies).json()	
    rdata = json.dumps(response)
    json_data = json.loads(rdata)
    return json_data

def get_expiry_dates():
    json_data = _do_request()
    return json_data['records']['expiryDates']

def get_expiry_range(expiry_date, range_strike=500):
    df_data = option_chain_data(expiry_date)

def option_chain_data(expiry_date, lot_size=50, strikes_range=2000):
    json_data = _do_request()
    ce_data = {}
    pe_data = {}
    num_ce_strikes = 0
    num_pe_strikes = 0
    strikes_diff = strikes_range//(lot_size*2)*lot_size

    for record in json_data['records']['data']:
        try:
            nearest_strike = (round(record['CE']['underlyingValue']/lot_size))*lot_size
            high_range_strike = (round(nearest_strike + strikes_diff)/lot_size)*lot_size
            low_range_strike = (round(nearest_strike - strikes_diff)/lot_size)*lot_size
        except:
            nearest_strike = (round(record['PE']['underlyingValue']/lot_size))*lot_size
        if record['expiryDate'] == expiry_date:
            if low_range_strike <= record['strikePrice'] and record['strikePrice'] <= high_range_strike:
                try:
                    ce_data[num_ce_strikes] = record['CE']
                    num_ce_strikes = num_ce_strikes + 1
                except:
                    pass
                try:
                    pe_data[num_pe_strikes] = record['PE']
                    num_pe_strikes = num_pe_strikes + 1
                except:
                    pass

    ce_df = pd.DataFrame.from_dict(ce_data).transpose()
    ce_df.columns +="_callopt"
    pe_df = pd.DataFrame.from_dict(pe_data).transpose()
    pe_df.columns +="_putopt"
    all_df = pd.concat([ce_df, pe_df],axis=1)
    all_df = all_df.drop(columns=['totalSellQuantity_callopt','totalSellQuantity_putopt','totalBuyQuantity_callopt','totalBuyQuantity_putopt','impliedVolatility_callopt','impliedVolatility_putopt','pChange_callopt','pChange_putopt','expiryDate_callopt', 'expiryDate_putopt', 'bidQty_putopt', 'bidprice_putopt', 'askQty_putopt', 'askPrice_putopt','bidQty_callopt', 'bidprice_callopt', 'askQty_callopt','askPrice_callopt', 'totalTradedVolume_callopt', 'totalTradedVolume_putopt','underlying_putopt','underlying_callopt', 'underlying_putopt','underlying_callopt','identifier_callopt','identifier_putopt'])
    return all_df

def main():
    today = str(date.today())
    end_time= datetime.fromisoformat(today + " " + '15:30')
    all_df = option_chain_data(expiry_date, strikes_range=500)
    all_df['time'] = datetime.now().strftime("%H:%M")
    conn = sql.connect('test.db')
    all_df.to_sql('nifty', conn,if_exists='append')

    conn = sql.connect('test.db')
    data = pd.read_sql('SELECT * FROM nifty', conn)
    print(data)
    '''
    while True:
        try:
            all_df = option_chain_data(expiry_date, strikes_range=500)
            all_df['time'] = datetime.datetime.now().time()
            print(all_df.loc[0])
            print("\n" +'*'*50 + "\n")
            sleep(60)
            if datetime.now() >= end_time:
                break
        except:
            pass
    '''


if __name__ == "__main__":
    main()
