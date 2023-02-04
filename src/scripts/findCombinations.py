from getTrains import getTrains
import datetime
import time as t

def getCombinations(source, junction, destination, date):
    # print(source, junction)
    fromSourceToJunction = getTrains(source, junction, date)
    # fromJunctionToDestination = getTrains(junction, destination, date)
    # print("Train from source to junction")
    # print(fromSourceToJunction)
    # print()
    # print(fromJunctionToDestination)
    # find combinations of trains from source to junction and from junction to destination 
    # that can be combined to reach destination from source
    # return the combinations in a list
    # print("Printing Combinations")
    combinations = []
    c = 0
    for firstTrain in fromSourceToJunction:
        c += 1
        if c == 5: break
        dateOfReachingJunction = convertTimeToEpoch(date, firstTrain['from_time']) + convertToSeconds(firstTrain['duration'])
        fromJunctionToDestination = getTrains(junction, destination, convertEpochTimeToDate(dateOfReachingJunction))
        for secondTrain in fromJunctionToDestination:
            combination = checkIfCombination(firstTrain, secondTrain, date, convertEpochTimeToDate(dateOfReachingJunction))
            if combination: combinations.append(combination)
    return combinations

def checkIfCombination(firstTrain, secondTrain, firstTrainDate, secondTrainDate):
    firstTrainFromTime = convertTimeToEpoch(firstTrainDate, firstTrain['from_time'])
    firstTrainToTime = firstTrainFromTime + convertToSeconds(firstTrain['duration'])
    secondTrainFromTime = convertTimeToEpoch(secondTrainDate, secondTrain['from_time'])
    secondTrainToTime = secondTrainFromTime + convertToSeconds(secondTrain['duration'])
    layoverTime = secondTrainFromTime - firstTrainToTime
    if layoverTime >= 0:
        combination = {
            "firstTrain": firstTrain,
            "secondTrain": secondTrain,
            "layoverTime": convertSecondsToHoursMinutes(layoverTime),
            "totalDuration": convertSecondsToHoursMinutes(secondTrainToTime - firstTrainFromTime),
            "time": secondTrainToTime - firstTrainFromTime
        }
        # convert combination to string and return
        return str(combination)

def convertTimeToEpoch(date, time):
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:])
    hour = int(time[:2])
    minute = int(time[3:5])
    return int(datetime.datetime(year, month, day, hour, minute).strftime('%s'))

def convertToSeconds(time):
    hour = int(time[:2])
    minute = int(time[3:5])
    return hour * 3600 + minute * 60

def convertEpochTimeToDate(epochTime):
    return datetime.datetime.fromtimestamp(epochTime).strftime('%Y%m%d')

def convertSecondsToHoursMinutes(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return str(hours) + "H:" + str(minutes) + "M"