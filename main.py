import re
from collections import Counter
from datetime import datetime
import statistics
import math


def getDateTime():
    # current date and time for the files
    now = datetime.now()

    timestamp = datetime.timestamp(now)

    dateTime = datetime.utcfromtimestamp(timestamp).strftime('%Y%m%d%H%M%S')

    return dateTime


def getFile(fileName):

    M = []
    f = open(fileName)
    with f:
        for line in f.readlines():
            for word in line.split():
                word = re.findall('[A-Za-z]+', word)
                if word:
                    M.append(word[0])

    S = list(set(M))

    return M, S


def wordsMedian(fileName):
    S, M = getFile(fileName)
    # sort in order with lowercase
    lower = [item.lower() for item in S]

    sortedS = sorted(lower)

    if(len(sortedS) % 2 == 0):
        med = int(len(sortedS)/2)

        f = open(getDateTime() + "median-" + fileName, "a")
        f.write("can't get a value since the median is between 2 indices, the median is between index: " +
                str(med) + " and " + str(med + 1))
    else:
        med = math.ceil(len(sortedS)/2)
        f = open(getDateTime() + "median.txt", "a")
        f.write("index: " + str(med) + ", value: " + sortedS[med])


def uniqueCount(fileName):
    M, S = getFile(fileName)

    f = open(getDateTime() + "count-" + fileName, "a")

    for i in S:
        count = 0
        for j in M:
            if i == j:
                count = count + 1

        if count > 1:
            f.write(i + " - number of occurrence: " + str(count) + "\n")
        else:
            f.write(i + "\n")


fileName = input("enter the name of the txt file that stores the tweets \n")

uniqueCount(fileName)
wordsMedian(fileName)
