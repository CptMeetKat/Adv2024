#!/usr/bin/python3

import sys

def main():

    if len(sys.argv) < 2:
        print("No input file provided")
        sys.exit(1)

    equasions = getData(sys.argv[1])

    result = 0
    for e in equasions:
        tester = int(e.split(":")[0])
        atoms = e.split(": ")[1].split(" ")
        terms = list(map(int, atoms))

        if permuteToTotal(tester, terms.copy(), 0):
            print("found: {}".format(tester))
            result += tester

    print("Result: {}".format(result))


def permuteToTotal(target, values, running_total):

    if running_total == target and len(values) == 0:
        return True
    if len(values) == 0:
        return False

    next = values.pop(0)
    if permuteToTotal(target, values.copy(), running_total + next):
        return True
    elif permuteToTotal(target, values.copy(), running_total * next):
        return True
    elif permuteToTotal(target, values.copy(), int("{}{}".format(running_total, next))):
        return True
    return False


def getData(filename):
    lines = []
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]
    return lines

if __name__ == "__main__":
    main()
