# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=C0103

from datetime import datetime

import pandas as pd

FII = "FII"
DII = "DII"
PRO = "Pro"
RETAIL = "Client"

class ParticipantData(object):
    def __init__(self, date=None):
        self.url = self.__geturl(date=date)
        self.DF = self.__fetch_and_load()
        self.processed_data = {}

    def check_sentiment(self,ttype):
        pos = []
        neg = []
        neutral = []
        if self.processed_data  == {}:
            self.end_of_day_data()
        data = self.processed_data
        for item in data:
            if data[item][ttype]['sentiment'] == 'Positive':
                pos.append(item)
            elif data[item][ttype]['sentiment'] == 'Negative':
                neg.append(item)
            else:
                neutral.append(item)
        return (pos,neg,neutral)

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
        self.processed_data = eod_data
        return eod_data

    def get_stock_futures_data(self):
        stk_fut_dicts = {"FII": {}, "DII": {}, "Pro": {}, "Client": {}}
        if self.DF is None:
            print("Data Not Found")
            return
        DF = self.DF
        DF = DF.drop(DF.index[0])
        DF = DF.drop(DF.index[-1])
        for _, row in DF.iterrows():
            stk_fut_dicts[row[0]]["long"] = int(row[3])
            stk_fut_dicts[row[0]]["short"] = int(row[4])
            difference = int(row[3]) - int(row[4])
            stk_fut_dicts[row[0]]["difference"] = difference
            if difference < 0:
                stk_fut_dicts[row[0]]["sentiment"] = "Negative"
            elif difference > 0:
                stk_fut_dicts[row[0]]["sentiment"] = "Positive"
            else:
                stk_fut_dicts[row[0]]["sentiment"] = "Neutral"
        return stk_fut_dicts

    def get_index_futures_data(self):
        fut_idx_dicts = {"FII": {}, "DII": {}, "Pro": {}, "Client": {}}
        if self.DF is None:
            print("Data Not Found")
            return
        DF = self.DF
        DF = DF.drop(DF.index[0])
        DF = DF.drop(DF.index[-1])
        for _, row in DF.iterrows():
            fut_idx_dicts[row[0]]["long"] = int(row[1])
            fut_idx_dicts[row[0]]["short"] = int(row[2])
            difference = int(row[1]) - int(row[2])
            fut_idx_dicts[row[0]]["difference"] = difference
            if difference < 0:
                fut_idx_dicts[row[0]]["sentiment"] = "Negative"
            elif difference > 0:
                fut_idx_dicts[row[0]]["sentiment"] = "Positive"
            else:
                fut_idx_dicts[row[0]]["sentiment"] = "Neutral"
        return fut_idx_dicts

    def get_index_option_ce_data(self):
        ce_opt_idx_dicts = {"FII": {}, "DII": {}, "Pro": {}, "Client": {}}
        if self.DF is None:
            print("Data Not Found")
            return
        DF = self.DF
        DF = DF.drop(DF.index[0])
        DF = DF.drop(DF.index[-1])
        for _, row in DF.iterrows():
            ce_opt_idx_dicts[row[0]]["long"] = int(row[5])
            ce_opt_idx_dicts[row[0]]["short"] = int(row[7])
            difference = int(row[5]) - int(row[7])
            ce_opt_idx_dicts[row[0]]["difference"] = difference
            if difference < 0:
                ce_opt_idx_dicts[row[0]]["sentiment"] = "Negative"
            elif difference > 0:
                ce_opt_idx_dicts[row[0]]["sentiment"] = "Positive"
            else:
                ce_opt_idx_dicts[row[0]]["sentiment"] = "Neutral"
        return ce_opt_idx_dicts

    def get_index_option_pe_data(self):
        pe_opt_idx_dicts = {"FII": {}, "DII": {}, "Pro": {}, "Client": {}}
        if self.DF is None:
            print("Data Not Found")
            return
        DF = self.DF
        DF = DF.drop(DF.index[0])
        DF = DF.drop(DF.index[-1])
        for _, row in DF.iterrows():
            pe_opt_idx_dicts[row[0]]["long"] = int(row[6])
            pe_opt_idx_dicts[row[0]]["short"] = int(row[8])
            difference = int(row[6]) - int(row[8])
            pe_opt_idx_dicts[row[0]]["difference"] = difference
            if difference > 0:
                pe_opt_idx_dicts[row[0]]["sentiment"] = "Negative"
            elif difference < 0:
                pe_opt_idx_dicts[row[0]]["sentiment"] = "Positive"
            else:
                pe_opt_idx_dicts[row[0]]["sentiment"] = "Neutral"
        return pe_opt_idx_dicts

    def get_stk_option_ce_data(self):
        ce_opt_stk_dicts = {"FII": {}, "DII": {}, "Pro": {}, "Client": {}}
        if self.DF is None:
            print("Data Not Found")
            return
        DF = self.DF
        DF = DF.drop(DF.index[0])
        DF = DF.drop(DF.index[-1])
        for _, row in DF.iterrows():
            ce_opt_stk_dicts[row[0]]["long"] = int(row[6])
            ce_opt_stk_dicts[row[0]]["short"] = int(row[8])
            difference = int(row[6]) - int(row[8])
            ce_opt_stk_dicts[row[0]]["difference"] = difference
            if difference < 0:
                ce_opt_stk_dicts[row[0]]["sentiment"] = "Negative"
            elif difference > 0:
                ce_opt_stk_dicts[row[0]]["sentiment"] = "Positive"
            else:
                ce_opt_stk_dicts[row[0]]["sentiment"] = "Neutral"
        return ce_opt_stk_dicts

    def get_stk_option_pe_data(self):
        pe_opt_stk_dicts = {"FII": {}, "DII": {}, "Pro": {}, "Client": {}}
        if self.DF is None:
            print("Data Not Found")
            return
        DF = self.DF
        DF = DF.drop(DF.index[0])
        DF = DF.drop(DF.index[-1])
        for _, row in DF.iterrows():
            pe_opt_stk_dicts[row[0]]["long"] = int(row[6])
            pe_opt_stk_dicts[row[0]]["short"] = int(row[8])
            difference = int(row[6]) - int(row[8])
            pe_opt_stk_dicts[row[0]]["difference"] = difference
            if difference > 0:
                pe_opt_stk_dicts[row[0]]["sentiment"] = "Negative"
            elif difference < 0:
                pe_opt_stk_dicts[row[0]]["sentiment"] = "Positive"
            else:
                pe_opt_stk_dicts[row[0]]["sentiment"] = "Neutral"
        return pe_opt_stk_dicts

    def __fetch_and_load(self):
        try:
            DF = pd.read_csv(self.url)
            DF = DF.transpose()
            DF = DF.drop(DF.index[-1])
            return DF.transpose()
        except Exception:
            return None

    def __geturl(self, date=None):
        if date is None:
            dnyformat = datetime.strftime(datetime.today(), "%d%m%Y")
        else:
            dnyformat = date
        return (
            "https://archives.nseindia.com/content/nsccl/fao_participant_oi_"
            + str(dnyformat)
            + ".csv"
        )
