import os
from sqlitedict import SqliteDict

DATABASE = "example.db"
INT_DAY_MAP = {
    'DAY1': 1,
    'DAY2': 2,
    'DAY3': 3,
    'DAY4': 4,
    'DAY5': 5,
}

iVALUE = {
            'ClientType': 'Client',
            'fut_idx_difference': 0,
            'fut_idx_long': '0',
            'fut_idx_short': '0',
            'fut_idx_signal': '-'
        }
nVALUE = {
            'ClientType': 'Client',
            'fut_idx_difference': 10010,
            'fut_idx_long': '162134',
            'fut_idx_short': '152124',
            'fut_idx_signal': 'Positive'
        }

def init_db():
    with SqliteDict(DATABASE) as db:
        for key in INT_DAY_MAP:
            update_db(INT_DAY_MAP[key], iVALUE)
        db.close()

def update_db(key, value):
    with SqliteDict(DATABASE) as db:
        db[key] = value
        db.commit()


def read_db(key=None):
    with SqliteDict(DATABASE) as db:
        for db_key, item in db.items():
            print("%s=%s" % (db_key, item))


def roll_data(new_value):
    with SqliteDict(DATABASE) as db:
        li = [ value for key, value in db.items()]
    li2 = [new_value] + li[:-1]
    for idx in range(1,6):
        update_db(idx, li2[idx-1])

if __name__ == '__main__':
    if not os.path.exists("./" + DATABASE):
        init_db()
    read_db()
    print("="*80)
    roll_data(nVALUE)
    read_db()
