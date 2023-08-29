#!/usr/bin/python3
"""Runner script for FNO data"""
import argparse
import json
import pprint
from datetime import date

from flask import jsonify

from dataWrapper import DatabaseRecorder as dr
from fnoData import DII
from fnoData import FII
from fnoData import ParticipantData as fno
from fnoData import PRO
from fnoData import RETAIL

DB_NAME = "../dbs/futureIndex.db"

if __name__ == "__main__":
    # db = dr(DB_NAME)
    # db.read_db()
    tdate = date.today()
    parser = argparse.ArgumentParser()
    parser.add_argument("--date","-d", default=tdate.strftime("%d%m%Y"))
    parser.add_argument('-t', '--data_type', default="ALL",)
    args = parser.parse_args()
    print(args.date)
    print("=" * 80)
    if args.data_type not in [
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

    today = fno(date=args.date)
    if args.data_type == "ALL":
        pprint.pprint(today.end_of_day_data())
    if args.data_type == "STK_FUT":
        pprint.pprint(today.get_stock_futures_data())
    if args.data_type == "IDX_FUT":
        pprint.pprint(today.get_index_futures_data())
    if args.data_type == "IDX_OPT_CE":
        pprint.pprint(today.get_index_option_ce_data())
    if args.data_type == "IDX_OPT_PE":
        pprint.pprint(today.get_index_option_pe_data())
    if args.data_type == "STK_OPT_CE":
        pprint.pprint(today.get_stk_option_ce_data())
    if args.data_type == "STK_OPT_PE":
        pprint.pprint(today.get_stk_option_pe_data())
    print("=" * 80)
