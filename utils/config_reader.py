import json
import os


def read_config():
    getdir = os.getcwd()
    filepath = getdir + "/utils/test_data.json"
    with open(filepath,"r+") as fread:
         readcontent = json.load(fread)
         return readcontent
