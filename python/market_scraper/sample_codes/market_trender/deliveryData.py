import pandas as pd
from datetime import datetime
import csv
import pprint

class StockDeliveryData(object):
    def __init__(self, date=None):
        self.url = self.__geturl(date=date)
        self.df = self.__fetch_and_load()

    def __fetch_and_load(self):
        df = pd.read_csv(self.url)
        df = df.drop(df.columns[[2,3,4,5,6,7,9,10,12]], axis=1)
        df = df[df[' SERIES'] ==  ' EQ']
        return df

    def __geturl(self, date=None):
        if date is None:
            dnyformat = datetime.strftime(datetime.today(), "%d%m%Y")
        else:
            dnyformat = date
        return (
            "https://archives.nseindia.com/products/content/sec_bhavdata_full_"
            + str(dnyformat)
            + ".csv"
        )

    def parse_data(self, percentage=0, last_price=10, turnover=1):
        delivery_data = []
        df = self.df
        df = df[df[' TURNOVER_LACS'] >= turnover]
        df = df[df[' CLOSE_PRICE'] >= last_price]
        df = df[df[' DELIV_PER'].astype(float) >= percentage]

        for index, row in df.iterrows():
            script_data = {}
            script_data['SYMBOL'] = row[0].strip()
            script_data['price'] = row[2]
            script_data['DELIV_PERCENTAGE'] = row[5].strip()
            delivery_data.append(script_data)
        return delivery_data

class FNOData(object):
    def __init__(self):
        self.df = self.__fetch_and_load()
        _list = list(self.df['SYMBOL    '])
        fno_list = [item.strip() for item in _list]
        fno_list.remove('Symbol')
        self.fno_list = fno_list

    def __fetch_and_load(self):
        df = pd.read_csv("https://archives.nseindia.com/content/fo/fo_mktlots.csv")
        return df

    def get_fno_symbols(self):
        return self.fno_list

    def get_fno_stocks_with_delivery_percentage(self, date=None, percentage=90):
        if date is None:
            date = datetime.strftime(datetime.today(), "%d%m%Y")
        today = StockDeliveryData(date=date)
        stk_data = today.parse_data(percentage=percentage)
        result = []
        for stk in stk_data:
            if stk['SYMBOL'] in self.fno_list:
                result.append(stk)
        return result
