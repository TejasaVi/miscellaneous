import pprint as pprint
from datetime import datetime
from datetime import timedelta

import pandas as pd


class FIIIndexDerivativeData(object):
    def __init__(self, date=None):
        self.root = {}
        self.__set_date()
        self.file_path = self.__get_filename(date=date)
        self.DF = self.__fetch_and_load()

    def __set_date(self):
        self.root['date'] = datetime.today().strftime('%Y-%m-%d')

    def __get_filename(self, date=None):
        if date is None:
            dnyformat = datetime.now() - timedelta(1)
            dnyformat = datetime.strftime(dnyformat, "%d-%b-%Y")
        else:
            dnyformat = date
            # "https://archives.nseindia.com/content/nsccl/fao_participant_oi_"
        self.file_path = "/home/terminator/fii_stats_" + \
            str(dnyformat) + ".xls"
        return self.file_path

    def __fetch_and_load(self):
        try:
            cols = [2, 4, 6]
            indexes = [0, 1, 2, 7, 8, 13, 14, 15, 16, 17, 18,
                       19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
            DF = pd.read_excel(self.file_path)
            DF.drop(DF.columns[cols], axis=1, inplace=True)
            DF.drop(index=indexes, inplace=True)
            return DF
        except FileNotFoundError:
            print("Data file not found, download the data file from NSE website")
        except Exception:
            print("Failed to intialize the data")

    def end_of_day_data(self):
        futures = {}
        options = {}
        DF = self.DF
        for idx in range(0, 4):
            futures[DF.iloc[idx, 0].lower().split(" ")[0]] = {}
            futures[DF.iloc[idx, 0].lower().split(
                " ")[0]]["buy"] = int(DF.iloc[idx, 1])
            futures[DF.iloc[idx, 0].lower().split(
                " ")[0]]["sell"] = int(DF.iloc[idx, 2])
            futures[DF.iloc[idx, 0].lower().split(" ")[0]]["net_contracts"] = int(
                DF.iloc[idx, 1]) - int(DF.iloc[idx, 2])
            futures[DF.iloc[idx, 0].lower().split(
                " ")[0]]["net_oi"] = int(DF.iloc[idx, 3])

        for idx in range(4, 8):
            options[DF.iloc[idx, 0].lower().split(" ")[0]] = {}
            options[DF.iloc[idx, 0].lower().split(
                " ")[0]]["buy"] = int(DF.iloc[idx, 1])
            options[DF.iloc[idx, 0].lower().split(
                " ")[0]]["sell"] = int(DF.iloc[idx, 1])
            options[DF.iloc[idx, 0].lower().split(" ")[0]]["net_contracts"] = int(
                DF.iloc[idx, 1]) - int(DF.iloc[idx, 2])
            options[DF.iloc[idx, 0].lower().split(
                " ")[0]]["net_oi"] = int(DF.iloc[idx, 3])
        self.root["futures"] = futures
        self.root["options"] = options
        return self.root


if __name__ == "__main__":
    data = FIIIndexDerivativeData()
    if data is not None:
        pprint.pprint(data.end_of_day_data())
    else:
        print("Failed to initialize the data")
