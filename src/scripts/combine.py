# read junctions from junctions.csv using csv module
import csv
from findCombinations import getCombinations
import sys

# with open('junctions.csv', 'r') as f:
#     reader = csv.reader(f)
#     junctions = list(reader)

# # read stations from stations.csv using csv module
# with open('stations.csv', 'r') as f:
#     reader = csv.reader(f)
#     stations = list(reader)

# # convert the stations list to a list of station codes
# stations = [station[2] for station in stations]
# junctions = [junction[0] for junction in junctions]

# source = 'New-Delhi-NDLS'
# destination = 'Indore-Jn-Bg-INDB'
# junction = 'Bhopal-Jn-BPL'
# date = '20230208'

date = sys.argv[1]
source = sys.argv[2]
destination = sys.argv[3]
# print(date, source, destination)

junctions = ['Itarsi-Jn-ET', 'Bhusaval-Jn-BSL', 'Bhopal-Jn-BPL']

allCombinations = []
for junction in junctions:
    combinations = getCombinations(source, junction, destination, date)
    allCombinations += combinations

# sort the combinations by time
allCombinations.sort(key=lambda x: eval(x)['time'])

print('{"combinations":[' + ",".join(allCombinations).replace("'", '"') + "]}")
sys.stdout.flush()