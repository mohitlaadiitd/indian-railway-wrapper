# read junctions from junctions.csv using csv module
import csv
with open('junctions.csv', 'r') as f:
    reader = csv.reader(f)
    junctions = list(reader)

# read stations from stations.csv using csv module
with open('stations.csv', 'r') as f:
    reader = csv.reader(f)
    stations = list(reader)

# convert the stations list to a list of station codes
stations = [station[2] for station in stations]
junctions = [junction[0] for junction in junctions]

# check if all the junctions are in the stations list
count = 0
for junction in junctions:
    if junction not in stations:
        print(junction)
        count += 1

print(count)