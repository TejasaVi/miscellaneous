#!/usr/bin/python3

from dataWrapper import DatabaseRecorder as dr
from fnoData import ParticipantData as fno
import pprint
import argparse
from flask import jsonify

dbName = "../dbs/futureIndex.db"

if __name__ == "__main__":
    #db = dr(dbName)
    #db.read_db()
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

    today = fno(date="15122022")
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
