import json
import os

class Configuration(object):
    def __init__(self, path=None):
        if path is None:
            self.path = ""
        else:
            self.path = path

    def read_config(self):
        if self.path and os.path.exists(self.path):
            with open(self.path) as json_data_file:
                self.cfg = json.load(json_data_file)
