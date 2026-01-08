
import sqlite3
import json


conn = sqlite3.connect('daily_derivatives_data.db')


create_futures_sql_queries = [
"CREATE TABLE  IF NOT EXISTS nifty_futures (datetime text PRIMARY KEY,contracts_buy integer,contracts_sell integer,net_contracts integer,net_oi integer);",
"CREATE TABLE  IF NOT EXISTS banknifty_futures (datetime text PRIMARY KEY,contracts_buy integer,contracts_sell integer,net_contracts integer,net_oi integer);",
"CREATE TABLE  IF NOT EXISTS finnifty_futures (datetime text PRIMARY KEY,contracts_buy integer,contracts_sell integer,net_contracts integer,net_oi integer);",
"CREATE TABLE  IF NOT EXISTS midcapnifty_futures (datetime text PRIMARY KEY,contracts_buy integer,contracts_sell integer,net_contracts integer,net_oi integer);",
]

create_options_sql_queries = [
"CREATE TABLE  IF NOT EXISTS nifty_options (datetime text PRIMARY KEY,contracts_buy integer,contracts_sell integer,net_contracts integer,net_oi integer);",
"CREATE TABLE  IF NOT EXISTS banknifty_options (datetime text PRIMARY KEY,contracts_buy integer,contracts_sell integer,net_contracts integer,net_oi integer);",
"CREATE TABLE  IF NOT EXISTS finnifty_options (datetime text PRIMARY KEY,contracts_buy integer,contracts_sell integer,net_contracts integer,net_oi integer);",
"CREATE TABLE  IF NOT EXISTS midcapnifty_options (datetime text PRIMARY KEY,contracts_buy integer,contracts_sell integer,net_contracts integer,net_oi integer);",
]

for query in create_futures_sql_queries:
    conn.execute(query)
    conn.commit()

for query in create_options_sql_queries:
    conn.execute(query)
    conn.commit()
conn.close()
