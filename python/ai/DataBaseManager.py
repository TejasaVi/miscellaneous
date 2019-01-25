#!/usr/bin/python

import sqlite3

class DataBaseManager(object):
    def __init__(self, path=None):
        if path:
            self.db_path = path
            self.initialized = True
        else:
            self.db_path = ""
        self.initialized = False

    def get_database_path(self):
        return self.db_path

    def set_db_path(path):
        self.db_path = path
        self.initialized = True

    def is_db_initialized(self):
        return self.initialized

    def get_db_connection(self):
        self.con = sqlite3.connect(self.db_path)
        return self.con

    def db_connection_close(self):
        self.con.close()

    def db_create_table(self, table_name, table_info):
        try:
            query = '''CREATE TABLE {0} ({1})'''.format(table_name,",".join(table_info))
            self.con.execute(query)
        except Exception as e:
            print ("table not created")
            print(e)

    def db_update_table(self, tables_name, column_values, task_id):
        try:
            res = []
            values = []
            for key, val in column_values.items():
                res.append("%s=?" %(str(key)))
                values.append(val)
            res = ', '.join(res)
            query = "UPDATE {0} SET {1} WHERE id=?".format(tables_name, res)
            values.append(task_id)
            self.con.execute(query,(values))
            self.con.commit()
        except Exception as e:
            print("Values not inserted into the tables")
            print (e)

    def db_insert_table(self, table_name, key_values):
        try:
            query = "INSERT INTO {0} {1} VALUES ({2}?)".format(table_name, tuple(key_values.keys()),"?, "*(len(key_values)-1))
            self.con.execute(query, tuple(key_values.values()))
            self.con.commit()
        except Exception as e:
            print("Values not inserted into the tables")
            print (e)

    def db_get_data(self, table_name, all_values=True, column_list=None,  where=None):
        try:
            if not all_values and column_list is None:
                raise("coloumn values not specified")
            column_list = "*" if all_values else column_list
            query = '''SELECT {0} FROM {1} '''.format( column_list, table_name )
            if where is not None:
                query = query + where
            cursor = self.con.execute(query)
            results = [row for row in cursor]
            return results
        except Exception as e:
            print (e)
