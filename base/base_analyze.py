import os

import yaml


def Analyze(fileName, className):
    with open("."+ str(os.sep)+ "data" + str(os.sep) + fileName, "r", encoding="utf-8") as f:
        data_list = list(yaml.safe_load(f)[className].values())
        print(data_list)
        return data_list