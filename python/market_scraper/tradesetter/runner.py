#!/usr/bin/python3
"""Runner script for FNO data"""
import argparse
import json
import pprint

from flask import jsonify

from dataWrapper import DatabaseRecorder as dr
from fnoData import ParticipantData as fno
from fnoData import FII,DII,RETAIL,PRO


DB_NAME = "../dbs/futureIndex.db"

if __name__ == "__main__":
    # db = dr(DB_NAME)
    # db.read_db()
    today = fno(date="28082023")
    today = today.end_of_day_data()
    print(today)
    pos, neg, neutral = today.check_sentiment(FII)
    print("FII positive on:", pos)
    print("FII negative on:", neg)
    print("FII Neutral on:", neutral)
    pos, neg, neutral = today.check_sentiment(RETAIL)
    print("RETAIL positive on:", pos)
    print("RETAIL negative on:", neg)
    print("RETAIL Neutral on:", neutral)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--data_type', default=None,)
    args = parser.parse_args()
    data_type = str(args.data_type)
    print("=" * 80)
    if data_type not in [
        "ALL",
        "STK_FUT",
        "IDX_FUT",
        "IDX_OPT_CE",
        "IDX_OPT_PE",
        "STK_OPT_CE",
        "STK_OPT_PE",
    ]:
        print("Invalid Option")
        print("=" * 80)
        exit(1)

    today = fno(date="25082023")
    if data_type == "ALL":
        pprint.pprint(today.end_of_day_data())
    if data_type == "STK_FUT":
        pprint.pprint(today.get_stock_futures_data())
    if data_type == "IDX_FUT":
        pprint.pprint(today.get_index_futures_data())
    if data_type == "IDX_OPT_CE":
        pprint.pprint(today.get_index_option_ce_data())
    if data_type == "IDX_OPT_PE":
        pprint.pprint(today.get_index_option_pe_data())
    if data_type == "STK_OPT_CE":
        pprint.pprint(today.get_stk_option_ce_data())
    if data_type == "STK_OPT_PE":
        pprint.pprint(today.get_stk_option_pe_data())
    print("=" * 80)
    """
