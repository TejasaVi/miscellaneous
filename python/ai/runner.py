#!/usr/bin/python
import datetime
import pprint as pprint
from collections import OrderedDict
from DataBaseManager import DataBaseManager
PATH = "./test.db"


db = DataBaseManager(path=PATH)
db.get_db_connection()
"""
table_info = "id integer primary key", "name text", "activity text", "time timestamp"
db.db_create_table("TIMEPASS",table_info)
dt = OrderedDict()
dt["name"]="tejas"
dt["activity"] = "lunch"
dt["time"] = datetime.datetime.now()
db.db_insert_table("TIMEPASS", dt)
db.con.commit()
res = db.db_get_data("TIMEPASS")
dt = OrderedDict()
dt["name"]="tejas"
dt["activity"] = "sleeping"
dt["time"] = datetime.datetime.now()
task_id = 12
db.db_update_table("TIMEPASS", dt ,task_id)
db.con.commit()
"""
column_list= "activity, time"
res = db.db_get_data("TIMEPASS", all_values=False, column_list=column_list, condition="name=='tejas'")
pprint.pprint(res)
db.db_connection_close()
