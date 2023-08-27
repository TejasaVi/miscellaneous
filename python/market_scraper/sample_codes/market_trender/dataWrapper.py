
import os
from sqlitedict import SqliteDict

ivalue = {
            'ClientType': '',
            'fut_idx_difference':0,
            'fut_idx_long':0,
            'fut_idx_short':0,
            'fut_idx_signal':'-'
        }

class DatabaseRecorder(object):
    def __init__(self, name):
        self.name= name
        self.location = "./dbs/" + self.name
        self.init_db()

    def init_db(self):
        if not os.path.exists(self.location):
            assert('database already exist')
        with SqliteDict(self.location) as ptr:
            for key in range(20):
                if key <5:
                    ivalue['ClientType'] = 'Client'
                    self.update_db(key,ivalue)
                elif key > 5 and key <10:
                    ivalue['ClientType'] = 'dii'
                    self.update_db(key,ivalue)
                elif key >10 and key  <15:
                    ivalue['ClientType'] = 'fii'
                    self.update_db(key,ivalue)
                else:
                    ivalue['ClientType'] = 'pro'
                    self.update_db(key,ivalue)
            ptr.commit()

    def update_db(self, key, value):
        with SqliteDict(self.location) as db:
            db[key] = value
            db.commit()

    def read_db(self):
        with SqliteDict(self.location) as db:
            for db_key, item in db.items():
                print("%s=%s" % (db_key, item))

    def roll_data(self, new_values):
        with SqliteDict(self.location) as db:
            li = [ value for key, value in db.items()]
        out_indices = [4,9,14,19]
        for idx in sorted(out_indices, reverse = True):
            del li[idx]
        in_indices = [0,5,10,15]
        for var in range(4):
            li.insert(var,new_values[var])
        for idx in range(20):
            update_db(idx, li[idx])

