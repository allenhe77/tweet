import re
from collections import Counter
from datetime import datetime

M = []
with open('tweet.txt') as f:
    for line in f.readlines():
        for word in line.split():
            word = re.findall('[A-Za-z]+', word)
            if word:
                M.append(word[0])

print(M)

S = list(set(M))


def getDateTime():
    # current date and time for the files
    now = datetime.now()

    timestamp = datetime.timestamp(now)

    dateTime = datetime.utcfromtimestamp(timestamp).strftime('%Y%m%d%H%M%S')

    return dateTime


def uniqueCount():
    f = open(getDateTime() + "count.txt", "a")

    for i in S:
        count = 0
        for j in M:
            if i == j:
                count = count + 1
        # only include count if > 1
        if count > 1:
            f.write(i + " - number of occurence: " + str(count) + "\n")
        else:
            f.write(i + "\n")


uniqueCount()
