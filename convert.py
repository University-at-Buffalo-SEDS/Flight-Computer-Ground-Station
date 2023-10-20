#!/bin/python3

# Converts a log file into a csv file

import json

with open("20230622T154952.log") as file:
    res = []
    lines = file.readlines()
    values = json.loads(lines[0])
    keys = list(values.keys())
    res.append((",".join(keys)))
    index = 0
    for l in lines:
        index += 1
        j_dump = json.loads(l)
        res.append("")
        for k in keys:
            res[index] = res[index] + str(j_dump[k]) + ","
        res[index] = res[index][:-1] + "\n"


with open("ground_station.csv", 'w') as file:
    file.writelines(res)