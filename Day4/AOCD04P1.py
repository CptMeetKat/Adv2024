#!/usr/bin/python3

import sys
import re


def getData(filename):
    lines = []
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]

    return lines

def main():
    if len(sys.argv) < 2:
        print("No input file provided")
        sys.exit(1)
    data = getData(sys.argv[1])

    result = 0
    x_max = len(data[0])
    y_max = len(data)


    result += horizontal(data, y_max)
    result += vertical(data, x_max, y_max)
    result += diagonalLeftRight(data, x_max, y_max)
    result += diagonalRightLeft(data, x_max, y_max)

    print("Result: {}".format(result))


def getTotalMatchesForward(text):
    return len(re.findall(r'(?<=XMAS)', text))

def getTotalMatchesBackward(text):
    return len(re.findall(r'(?<=SAMX)', text))

def horizontal(block, y_max):
    
    total = 0
    for y in range(y_max):
        line = block[y]
        total += getTotalMatchesForward(line)
        total += getTotalMatchesBackward(line)
            
    return total

def vertical(block, x_max, y_max):

    total = 0

    for x in range(x_max):
        string_parts = []
        for y in range(y_max):
            string_parts.append(block[y][x])
        line = "".join(string_parts)
        total += getTotalMatchesForward(line)
        total += getTotalMatchesBackward(line)
            
    return total

def diagonalLeftRight(block, x_max, y_max):

    starts = []
    for y in range(1, y_max):
        starts.append((0, y))
    for x in range(x_max):
        starts.append((x, 0))


    total = 0
    for start in starts:
        string_parts = []
        x = start[0]
        y = start[1]
        while x < x_max and y < y_max:
            string_parts.append(block[y][x])
            x+=1
            y+=1
        line = "".join(string_parts)
        total += getTotalMatchesForward(line)
        total += getTotalMatchesBackward(line)
    
    return total

def diagonalRightLeft(block, x_max, y_max):

    starts = []
    for y in range(0, y_max-1):
        starts.append((0, y))
    for x in range(x_max):
        starts.append((x, y_max-1))


    total = 0
    for start in starts:
        string_parts = []
        x = start[0]
        y = start[1]
        while x < x_max and y >= 0:
            string_parts.append(block[y][x])
            x+=1
            y-=1
        line = "".join(string_parts)
        total += getTotalMatchesForward(line)
        total += getTotalMatchesBackward(line)
    
    return total


if __name__ == "__main__":
    main()
