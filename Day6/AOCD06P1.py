#!/usr/bin/python3

import sys

def parseInput(filename):
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            lines.append(list(line.strip()))

    return lines

def main():
    if len(sys.argv) < 2:
        print("No input file provided")
        sys.exit(1)
    map = parseInput(sys.argv[1])

    start_x, start_y = getStartPosition(map)
    traverse(map, start_x, start_y)

    result = countUniqueSteps(map)
    #printMap(map)
    print("Result: {}".format(result))


def traverse(map, start_x, start_y):
    direction = 0 #0 up, 1 right, 2 down, left 3
    x,y = start_x, start_y
    prev_x, prev_y = x, y
    
    map[y][x] = "x"
    x, y = move(direction, x, y)
    while inRange(map, x, y):

        if map[y][x] == "#":
            direction = turn(direction)
            x,y = prev_x, prev_y
        else:
            map[y][x] = "x"
            prev_x, prev_y = x, y

        x, y = move(direction, x, y)



def printMap(map):

    for y in range(len(map)):
        for x in range(len(map[0])):
            print(map[y][x], end="")
        print()
    print()


def move(direction, x, y):

    if direction == 0:
        y-=1           
    elif direction == 1:
        x+=1
    elif direction == 2:
        y+=1
    elif direction == 3:
        x-=1
    return x, y


def inRange(map, x, y):
    max_x = len(map[0])
    max_y = len(map)

    return x >= 0 and x < max_x and y >= 0 and y < max_y

def turn(direction):
    direction+=1
    return direction % 4


def countUniqueSteps(map):
    total = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == "x":
                total+=1
    return total

def getStartPosition(map):
    
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == "^":
                return x,y

    return -1,-1


if __name__ == "__main__":
    main()
