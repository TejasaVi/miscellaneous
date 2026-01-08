import csv
import json
from enum import Enum


class DataStore:
    class DataType(Enum):
        csv = 1
        api = 2
        excel = 3
        json = 4
        py_dict = 5

    def __init__(self, d_type, key, inputFile=None, DestFile=None):
        if inputFile:
            self.source = inputFile
        self.type = d_type
        if DestFile:
            self.json_dest = DestFile
        self.data_key = key
        self.data_values = {}

    def __repr__(self):
        return

    def return_json(self):
        data = {}
        with open(self.source, encoding="utf-8") as csvf:
            csvReader = csv.DictReader(csvf)
            for row in csvReader:
                key = row.pop(self.data_key)
                data[key] = row
        return data

    def return_jsonfile(self):
        data = {}
        if self.json_dest:
            with open(self.source, encoding="utf-8") as csvf:
                csvReader = csv.DictReader(csvf)
                for row in csvReader:
                    key = row.pop(self.data_key)
                    data[key] = row
            with open(self.json_dest, 'w', encoding='utf-8') as jsonf:
                jsonf.write(json.dumps(data, indent=4))
        else:
            # DestFile not Set
            return

    def return_py_dict(self):
        with open(self.source, encoding="utf-8") as csvf:
            csvReader = csv.DictReader(csvf)
            for row in csvReader:
                key = row.pop(self.data_key)
                data[key] = row
        return data

