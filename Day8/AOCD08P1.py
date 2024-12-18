#!/usr/bin/python3

import sys
from collections import namedtuple

max_width=0
max_height=0

Coordinate = namedtuple("Coordinate", ["x","y"])

def main():
    if len(sys.argv) < 2:
        print("No input file provided")
        sys.exit(1)

    run(sys.argv[1])
    
def run(filename):

    global max_height, max_width;

    map = getData(filename)
    max_height = len(map)
    max_width = len(map[0])

    antinodes = generateAntiNodes(map)

    result = len(antinodes)
    print("Result: {}".format(result))

def printMap(map):
    global max_height, max_width;
    for y in range(max_height):
        for x in range(max_width):
            print(map[y][x], end="")
        print()
    print()

def printAntiNodes(antinodes):
    global max_height, max_width;
    for y in range(max_height):
        for x in range(max_width):
            if (x,y) in antinodes:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()


def generateAntiNodes(map):
    antinodes = set()
    antennas = findNodeLocations(map)
    for k in antennas.keys():
        positions = antennas[k]
        for pos_a in range(len(positions)-1):
            for pos_b in range(pos_a+1, len(positions)):
                antennaA = positions[pos_a]
                antennaB = positions[pos_b]
                nodes = createAntiNodes(antennaA, antennaB) 
                for elt in nodes:
                    antinodes.add((elt.x,elt.y))

    return antinodes

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def gradientDirection(a,b):
    return sign(   (b[1]-a[1])) / ((b[0]-a[0]))

def getLeftNode(a,b):
    if a.x < b.x:
        return a;
    else:
        return b

def getRightNode(a,b):
    if a.x >= b.x:
        return a;
    else:
        return b

def getUpNode(a,b):
    if a.y < b.y:
        return a;
    else:
        return b

def getDownNode(a,b):
    if a.y >= b.y:
        return a;
    else:
        return b

def createAntiNodes(antennaA, antennaB):
    antinodes = []

    left = getLeftNode(antennaA, antennaB)
    right = getRightNode(antennaA, antennaB)
    up = getUpNode(antennaA, antennaB)
    down = getDownNode(antennaA, antennaB)


    x_diff = abs(left.x - right.x)
    y_diff = abs(left.y - right.y)

    if antennaA.x == antennaB.x:
        x_diff = abs(up.x - down.x)
        y_diff = abs(up.y - down.y)
        antinodes.append(Coordinate(up.x, up.y-y_diff))
        antinodes.append(Coordinate(down.x, down.y+y_diff))
    if antennaA.y == antennaB.y:
        antinodes.append(Coordinate(left.x - x_diff, left.y+y_diff))
        antinodes.append(Coordinate(right.x + x_diff, right.y-y_diff))
    else:
        slope = gradientDirection(left, right)
        if slope < 0: # / gradient
            antinodes.append(Coordinate(left.x - x_diff, left.y+y_diff))
            antinodes.append(Coordinate(right.x + x_diff, right.y-y_diff))
        else: # \ gradient
            antinodes.append(Coordinate(left.x - x_diff, left.y-y_diff))
            antinodes.append(Coordinate(right.x + x_diff, right.y+y_diff))

    antinodes = [n for n in antinodes if inRange(n.x, n.y) ]

    return antinodes


def findNodeLocations(map):

    global max_height, max_width;

    locations = {}
    for y in range(max_height):
        for x in range(max_width):
            char = map[y][x]
            if char != "." :
                if char in locations:
                    locations[char].append(Coordinate(x,y))
                else:
                    locations[char] = [Coordinate(x,y)]
    return locations


def inRange(x,y):
    global max_height, max_width;
    return x < max_width and x >= 0 and y < max_height and y >= 0

def getData(filename):
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            lines.append(list(line.strip()))

    return lines

if __name__ == "__main__":
    main()
