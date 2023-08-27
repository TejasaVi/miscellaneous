import json
import pandas as pd
from datetime import datetime
import csv
import pprint
#dnyformat = datetime.strftime(datetime.today(), "%d%m%Y")
#url = "https://www1.nseindia.com/content/nsccl/fao_participant_oi_" + str(dnyformat) + ".csv"


def get_stock_future_data(df):
    stk_fut_dicts = {}
    stk_fut_dicts["stock_futures"]={}
    df = df.drop(df.index[0])
    df = df.drop(df.index[-1])
    for index, row in df.iterrows():
        client_dict = {}
        client_type = row[0]
        stk_fut_dicts["stock_futures"][client_type] = {}
        client_dict['stk_fut_long'] = row[3]
        client_dict['stk_fut_short'] = row[4]
        difference = int(row[3]) - int(row[4])
        client_dict['stk_fut_difference'] = difference
        if difference < 0:
            client_dict['stk_fut_signal'] = 'Negative'
        elif difference >0:
            client_dict['stk_fut_signal'] = 'Positive'
        else:
            client_dict['stk_fut_signal'] = 'Neutral'
        stk_fut_dicts["stock_futures"][client_type] =client_dict
    return stk_fut_dicts

def get_future_index_data(df):
    fut_idx_dicts = {}
    fut_idx_dicts["index_futures"] = {}
    df = df.drop(df.index[0])
    df = df.drop(df.index[-1])
    for index, row in df.iterrows():
        client_dict = {}
        client_type = row[0]
        fut_idx_dicts["index_futures"][client_type] = {}
        client_dict['fut_idx_long'] = row[1]
        client_dict['fut_idx_short'] = row[2]
        difference = int(row[1]) - int(row[2])
        client_dict['fut_idx_difference'] = difference
        if difference < 0:
            client_dict['fut_idx_signal'] = 'Negative'
        elif difference >0:
            client_dict['fut_idx_signal'] = 'Positive'
        else:
            client_dict['fut_idx_signal'] = 'Neutral'
        fut_idx_dicts["index_futures"][client_type]=client_dict
    return fut_idx_dicts

def get_ce_option_index_data(df):
    ce_opt_idx_dicts = {}
    ce_opt_idx_dicts["index_option_ce"] = {}
    df = df.drop(df.index[0])
    df = df.drop(df.index[-1])
    for index, row in df.iterrows():
        client_dict = {}
        client_type = row[0]
        ce_opt_idx_dicts["index_option_ce"][client_type] = {}
        client_dict['ce_opt_idx_long'] = row[5]
        client_dict['ce_opt_idx_short'] = row[7]
        difference = int(row[5]) - int(row[7])
        client_dict['ce_opt_idx_difference'] = difference
        if difference < 0:
            client_dict['ce_opt_idx_signal'] = 'Negative'
        elif difference >0:
            client_dict['ce_opt_idx_signal'] = 'Positive'
        else:
            client_dict['ce_opt_idx_signal'] = 'Neutral'
        ce_opt_idx_dicts["index_option_ce"][client_type] = client_dict
    return ce_opt_idx_dicts

def get_pe_option_index_data(df):
    pe_opt_idx_dicts = {}
    pe_opt_idx_dicts["index_option_pe"]={}

    df = df.drop(df.index[0])
    df = df.drop(df.index[-1])
    for index, row in df.iterrows():
        client_dict = {}
        client_type = row[0]
        pe_opt_idx_dicts["index_option_pe"][client_type]={}
        client_dict['pe_opt_idx_long'] = row[6]
        client_dict['pe_opt_idx_short'] = row[8]
        difference = int(row[6]) - int(row[8])
        client_dict['pe_opt_idx_difference'] = difference
        if difference > 0:
            client_dict['pe_opt_idx_signal'] = 'Negative'
        elif difference < 0:
            client_dict['pe_opt_idx_signal'] = 'Positive'
        else:
            client_dict['pe_opt_idx_signal'] = 'Neutral'
        pe_opt_idx_dicts["index_option_pe"][client_type] = client_dict
    return pe_opt_idx_dicts

def get_stk_ce_option_data(df):
    ce_opt_stk_dicts = {}
    ce_opt_stk_dicts["stock_option_ce"] = {}
    df = df.drop(df.index[0])
    df = df.drop(df.index[-1])
    for index, row in df.iterrows():
        client_dict = {}
        client_type = row[0]
        ce_opt_stk_dicts["stock_option_ce"][client_type] = {}
        client_dict['pe_opt_stk_long'] = row[6]
        client_dict['pe_opt_stk_short'] = row[8]
        difference = int(row[6]) - int(row[8])
        client_dict['pe_opt_stk_difference'] = difference
        if difference < 0:
            client_dict['pe_opt_stk_signal'] = 'Negative'
        elif difference >0:
            client_dict['pe_opt_stk_signal'] = 'Positive'
        else:
            client_dict['pe_opt_stk_signal'] = 'Neutral'
        ce_opt_stk_dicts["stock_option_ce"][client_type] = client_dict
    return ce_opt_stk_dicts

def get_stk_pe_option_data(df):
    pe_opt_stk_dicts = {}
    pe_opt_stk_dicts["stock_option_pe"] = {}
    df = df.drop(df.index[0])
    df = df.drop(df.index[-1])
    for index, row in df.iterrows():
        client_dict = {}
        client_type = row[0]
        pe_opt_stk_dicts["stock_option_pe"][client_type] = {}
        client_dict['pe_opt_stk_long'] = row[6]
        client_dict['pe_opt_stk_short'] = row[8]
        difference = int(row[6]) - int(row[8])
        client_dict['pe_opt_stk_difference'] = difference
        if difference > 0:
            client_dict['pe_opt_stk_signal'] = 'Negative'
        elif difference < 0:
            client_dict['pe_opt_stk_signal'] = 'Positive'
        else:
            client_dict['pe_opt_stk_signal'] = 'Neutral'
        pe_opt_stk_dicts["stock_option_pe"][client_type] = client_dict
    return pe_opt_stk_dicts

def main():
    url = "https://archives.nseindia.com/content/nsccl/fao_participant_oi_25082023.csv"
    df = pd.read_csv(url)
    df = df.transpose()
    df = df.drop(df.index[-1])
    df = df.transpose()
    '''
    for index, row in df.iterrows():
        print(row[0],row[2],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14])
    '''
    d1 = get_future_index_data(df)
    d2 = get_stock_future_data(df)
    d3 = get_ce_option_index_data(df)
    d4 = get_pe_option_index_data(df)
    d5 = get_stk_ce_option_data(df)
    d6 = get_stk_pe_option_data(df)
    d7 = d1|d2|d3|d4|d5|d6
    print(json.dumps(d7))

if __name__ == '__main__':
    main()
