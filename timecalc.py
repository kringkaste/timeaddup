import time

def calc(string):
    tokens = string.split()

    startDate = None
    endDate = None
    sumTime = 0

    for token in tokens:
        if "m" in token:
            value = token.replace("m", "").replace("+", "").replace("-", "")
            if "-" in token:
                sumTime = sumTime - (int(value) * 60)
            else:
                sumTime = sumTime + (int(value) * 60)
        elif startDate == None:
            startDate = time.strptime(token, "%H:%M")
        else:
            endDate = time.strptime(token, "%H:%M")
            diff = time.mktime(endDate) - time.mktime(startDate)
            sumTime = sumTime + diff
            startDate = None
            endDate = None

    sumTime = sumTime / 60 / 60

    result = "%.2f" % sumTime
    return result.replace(".", ",")