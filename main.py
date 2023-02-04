import csv 
import json

with open('stations.csv', 'r') as f:
    reader = csv.reader(f)
    stations = list(reader)
# convert the stations list to a list of station codes
stations = [[station[1], station[0]] for station in stations]
selectOptions = []
for station in stations:
    name = station[0]
    code = station[1]
    # replace junction if present in name to Jn
    if 'Junction' in name:
        name = name.replace('Junction', 'Jn')
    selectOptions.append({'label': name + ' (' + code + ')', 'value': name.replace(' ', '-') + '-' + code})

# write this selectOptions list to a json file
with open('stations.json', 'w') as f:
    json.dump(selectOptions, f)