import pandas as pd
from datetime import datetime
import csv
import pprint


class ParticipantData(object):
    def __init__(self, date=None):
        self.url = self.__geturl(date=date)
        self.df = self.__fetch_and_load()

    def end_of_day_data(self):
        eod_data = {
            "index_futures": {},
            "stock_futures": {},
            "index_call_options": {},
            "index_put_options": {},
            "stock_call_options": {},
            "stock_put_options": {},
        }
        eod_data["index_futures"] = self.get_index_futures_data()
        eod_data["stock_futures"] = self.get_stock_futures_data()
        eod_data["index_call_options"] = self.get_index_option_ce_data()
        eod_data["index_put_options"] = self.get_index_option_pe_data()
        eod_data["stock_call_options"] = self.get_stk_option_ce_data()
        eod_data["stock_put_options"] = self.get_stk_option_pe_data()
        return eod_data

    def get_stock_futures_data(self):
        stk_fut_dicts = {"FII": {}, "DII": {}, "Pro": {}, "Client": {}}
        if self.df is None:
            print("Data Not Found")
            return
        df = self.df
        df = df.drop(df.index[0])
        df = df.drop(df.index[-1])
        for index, row in df.iterrows():
            stk_fut_dicts[row[0]]["stk_fut_long"] = int(row[3])
            stk_fut_dicts[row[0]]["stk_fut_short"] = int(row[4])
            difference = int(row[3]) - int(row[4])
            stk_fut_dicts[row[0]]["stk_fut_difference"] = difference
            if difference < 0:
                stk_fut_dicts[row[0]]["stk_fut_signal"] = "Negative"
            elif difference > 0:
                stk_fut_dicts[row[0]]["stk_fut_signal"] = "Positive"
            else:
                stk_fut_dicts[row[0]]["stk_fut_signal"] = "Neutral"
        return stk_fut_dicts

    def get_index_futures_data(self):
        fut_idx_dicts = {"FII": {}, "DII": {}, "Pro": {}, "Client": {}}
        if self.df is None:
            print("Data Not Found")
            return
        df = self.df
        df = df.drop(df.index[0])
        df = df.drop(df.index[-1])
        for index, row in df.iterrows():
            fut_idx_dicts[row[0]]["fut_idx_long"] = int(row[1])
            fut_idx_dicts[row[0]]["fut_idx_short"] = int(row[2])
            difference = int(row[1]) - int(row[2])
            fut_idx_dicts[row[0]]["fut_idx_difference"] = difference
            if difference < 0:
                fut_idx_dicts[row[0]]["fut_idx_signal"] = "Negative"
            elif difference > 0:
                fut_idx_dicts[row[0]]["fut_idx_signal"] = "Positive"
            else:
                fut_idx_dicts[row[0]]["fut_idx_signal"] = "Neutral"
        return fut_idx_dicts

    def get_index_option_ce_data(self):
        ce_opt_idx_dicts = {"FII": {}, "DII": {}, "Pro": {}, "Client": {}}
        if self.df is None:
            print("Data Not Found")
            return
        df = self.df
        df = df.drop(df.index[0])
        df = df.drop(df.index[-1])
        for index, row in df.iterrows():
            ce_opt_idx_dicts[row[0]]["ce_opt_idx_long"] = int(row[5])
            ce_opt_idx_dicts[row[0]]["ce_opt_idx_short"] = int(row[7])
            difference = int(row[5]) - int(row[7])
            ce_opt_idx_dicts[row[0]]["ce_opt_idx_difference"] = difference
            if difference < 0:
                ce_opt_idx_dicts[row[0]]["ce_opt_idx_signal"] = "Negative"
            elif difference > 0:
                ce_opt_idx_dicts[row[0]]["ce_opt_idx_signal"] = "Positive"
            else:
                ce_opt_idx_dicts[row[0]]["ce_opt_idx_signal"] = "Neutral"
        return ce_opt_idx_dicts

    def get_index_option_pe_data(self):
        pe_opt_idx_dicts = {"FII": {}, "DII": {}, "Pro": {}, "Client": {}}
        if self.df is None:
            print("Data Not Found")
            return
        df = self.df
        df = df.drop(df.index[0])
        df = df.drop(df.index[-1])
        for index, row in df.iterrows():
            pe_opt_idx_dicts[row[0]]["pe_opt_idx_long"] = int(row[6])
            pe_opt_idx_dicts[row[0]]["pe_opt_idx_short"] = int(row[8])
            difference = int(row[6]) - int(row[8])
            pe_opt_idx_dicts[row[0]]["pe_opt_idx_difference"] = difference
            if difference > 0:
                pe_opt_idx_dicts[row[0]]["pe_opt_idx_signal"] = "Negative"
            elif difference < 0:
                pe_opt_idx_dicts[row[0]]["pe_opt_idx_signal"] = "Positive"
            else:
                pe_opt_idx_dicts[row[0]]["pe_opt_idx_signal"] = "Neutral"
        return pe_opt_idx_dicts

    def get_stk_option_ce_data(self):
        ce_opt_stk_dicts = {"FII": {}, "DII": {}, "Pro": {}, "Client": {}}
        if self.df is None:
            print("Data Not Found")
            return
        df = self.df
        df = df.drop(df.index[0])
        df = df.drop(df.index[-1])
        for index, row in df.iterrows():
            ce_opt_stk_dicts[row[0]]["pe_opt_stk_long"] = int(row[6])
            ce_opt_stk_dicts[row[0]]["pe_opt_stk_short"] = int(row[8])
            difference = int(row[6]) - int(row[8])
            ce_opt_stk_dicts[row[0]]["pe_opt_stk_difference"] = difference
            if difference < 0:
                ce_opt_stk_dicts[row[0]]["pe_opt_stk_signal"] = "Negative"
            elif difference > 0:
                ce_opt_stk_dicts[row[0]]["pe_opt_stk_signal"] = "Positive"
            else:
                ce_opt_stk_dicts[row[0]]["pe_opt_stk_signal"] = "Neutral"
        return ce_opt_stk_dicts

    def get_stk_option_pe_data(self):
        pe_opt_stk_dicts = {"FII": {}, "DII": {}, "Pro": {}, "Client": {}}
        if self.df is None:
            print("Data Not Found")
            return
        df = self.df
        df = df.drop(df.index[0])
        df = df.drop(df.index[-1])
        for index, row in df.iterrows():
            pe_opt_stk_dicts[row[0]]["pe_opt_stk_long"] = int(row[6])
            pe_opt_stk_dicts[row[0]]["pe_opt_stk_short"] = int(row[8])
            difference = int(row[6]) - int(row[8])
            pe_opt_stk_dicts[row[0]]["pe_opt_stk_difference"] = difference
            if difference > 0:
                pe_opt_stk_dicts[row[0]]["pe_opt_stk_signal"] = "Negative"
            elif difference < 0:
                pe_opt_stk_dicts[row[0]]["pe_opt_stk_signal"] = "Positive"
            else:
                pe_opt_stk_dicts[row[0]]["pe_opt_stk_signal"] = "Neutral"
        return pe_opt_stk_dicts

    def __fetch_and_load(self):
        try:
            df = pd.read_csv(self.url)
            df = df.transpose()
            df = df.drop(df.index[-1])
            return df.transpose()
        except Exception as ex:
            return None

    def __geturl(self, date=None):
        if date is None:
            dnyformat = datetime.strftime(datetime.today(), "%d%m%Y")
        else:
            dnyformat = date
        return (
            "https://www1.nseindia.com/content/nsccl/fao_participant_oi_"
            + str(dnyformat)
            + ".csv"
        )
