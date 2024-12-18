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
    antennas = findAntennaLocations(map)
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
    right = getRightNode(a,b)
    left = getLeftNode(a,b)
    return sign(   (right[1]-left[1])) / ((right[0]-left[0]))

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


    if antennaA.x == antennaB.x:
        antinodes += createVerticalAntinodes(antennaA, antennaB)
    elif antennaA.y == antennaB.y:
        antinodes += createHorizontalAntinodes(antennaA, antennaB)
    else:
        if gradientDirection(antennaA, antennaB) < 0: #/
            antinodes += createAscAntinodes(antennaA, antennaB)
        else: #\
            antinodes += createDescAntinodes(antennaA, antennaB)
    antinodes = [n for n in antinodes if inRange(n.x, n.y) ]

    return antinodes

def createDescAntinodes(antennaA, antennaB):
    antinodes = []
    left = getLeftNode(antennaA, antennaB)
    right = getRightNode(antennaA, antennaB)

    x_diff = abs(left.x - right.x)
    y_diff = abs(left.y - right.y)

    x_mod = 0
    y_mod = 0

    while inRange(left.x - x_mod, left.y-y_mod) or inRange(right.x + x_mod, right.y+y_mod):
        antinodes.append(Coordinate(left.x - x_mod, left.y-y_mod))
        antinodes.append(Coordinate(right.x + x_mod, right.y+y_mod))
        x_mod += x_diff
        y_mod += y_diff

    return antinodes


def createAscAntinodes(antennaA, antennaB):
    antinodes = []
    left = getLeftNode(antennaA, antennaB)
    right = getRightNode(antennaA, antennaB)

    x_diff = abs(left.x - right.x)
    y_diff = abs(left.y - right.y)

    x_mod = 0
    y_mod = 0

    while inRange(left.x - x_mod, left.y+y_mod) or inRange(right.x + x_mod, right.y-y_mod):
        antinodes.append(Coordinate(left.x - x_mod, left.y+y_mod))
        antinodes.append(Coordinate(right.x + x_mod, right.y-y_mod))
        x_mod += x_diff
        y_mod += y_diff

    return antinodes

def createHorizontalAntinodes(antennaA, antennaB):
    antinodes = []

    left = getLeftNode(antennaA, antennaB)
    right = getRightNode(antennaA, antennaB)
    x_diff = abs(left.x - right.x)
    y_diff = abs(left.y - right.y)

    x_mod = 0
    y_mod = 0

    while inRange(left.x - x_mod, left.y+y_mod) or inRange(right.x + x_mod, right.y-y_mod):

        antinodes.append(Coordinate(left.x - x_mod, left.y+y_mod))
        antinodes.append(Coordinate(right.x + x_mod, right.y-y_mod))
        x_mod += x_diff
        y_mod += y_diff

    return antinodes

def createVerticalAntinodes(antennaA, antennaB):
    antinodes = []

    up = getUpNode(antennaA, antennaB)
    down = getDownNode(antennaA, antennaB)
    y_diff = abs(up.y - down.y)

    modifier = 0
    while inRange(up.x, up.y-modifier) or inRange(down.x, down.y+modifier):
        antinodes.append(Coordinate(up.x, up.y-modifier))
        antinodes.append(Coordinate(down.x, down.y+modifier))
        modifier += y_diff

    return antinodes
    

def findAntennaLocations(map):

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
