#!/usr/bin/python3

import sys


def getData(filename):
    content = ""
    with open(filename, 'r') as file:
        content = file.read()
    return content.strip()


def main():
    if len(sys.argv) < 2:
        print("No input file provided")
        sys.exit(1)
    data = getData(sys.argv[1])

    safe_reports = 0

    for line in data.split("\n"):
        values = line.split()

        if isSafe(values):
            safe_reports+=1

    print("Result: {}".format(safe_reports))

def isSafe(values):

    if not isIncreasing(values):
        for i in range(len(values)):
            popped = values.pop(i)
            if isIncreasing(values):
                return True
            values.insert(i, popped)
    else:
        return True


    if not isDecreasing(values):
        for i in range(len(values)):
            popped = values.pop(i)
            if isDecreasing(values):
                return True
            values.insert(i, popped)
    else:
        return True

    return False

def isIncreasing(numbers):
    for i in range(len(numbers)-1):
        a = int(numbers[i])
        b = int(numbers[i+1])
        difference = abs(a-b)

        if a > b or difference < 1 or difference > 3:
            return False
    return True

def isDecreasing(numbers):
    for i in range(len(numbers)-1):
        a = int(numbers[i])
        b = int(numbers[i+1])
        difference = abs(a-b)

        if a < b or difference < 1 or difference > 3:
            return False
    return True


if __name__ == "__main__":
    main()


