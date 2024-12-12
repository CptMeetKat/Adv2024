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
    path = traverse(map, start_x, start_y)
    
    found = set()
    for i in range(0, len(path)):
        x = path[i][0] 
        y = path[i][1]
        direction = path[i][2]
        obstruction_x, obstruction_y = move(direction,x,y)

        if inRange(map, obstruction_x, obstruction_y) and map[obstruction_y][obstruction_x] == "#":
            direction = turn(direction)
            obstruction_x, obstruction_y = move(direction,x,y)
        if inRange(map, obstruction_x, obstruction_y) and not (obstruction_x == start_x and obstruction_y == start_y):
            map[obstruction_y][obstruction_x] = "O"

            path_type = traverse_with_obstruction(map, start_x, start_y, (obstruction_x, obstruction_y))
            if path_type == 1:
                found.add("{},{}".format(obstruction_x, obstruction_y))

    print("Result: {}".format(len(found)))

def traverse(map, start_x, start_y):
    direction = 0 #0 up, 1 right, 2 down, left 3
    x,y = start_x, start_y
    prev_x, prev_y = x, y
    
    path = []
    path.append((x,y,direction))
    map[y][x] = "x"
    x, y = move(direction, x, y)
    while inRange(map, x, y) and not (x == start_x and y == start_y and direction == 0):
        if map[y][x] == "#":
            direction = turn(direction)
            x,y = prev_x, prev_y
        else:
            map[y][x] = "x"
            prev_x, prev_y = x, y
            path.append((x,y,direction))

        x, y = move(direction, x, y)

    return path


def traverse_with_obstruction(map, start_x, start_y, obstruction=None):

    path_type = 0 # 0: terminating, 1: looping

    visited = set()
    direction = 0 #0 up, 1 right, 2 down, left 3
    x,y = start_x, start_y
    prev_x, prev_y = x, y
    
    visited.add("{},{},{}".format(x,y,direction))
    x, y = move(direction, x, y)
    while inRange(map, x, y) and ("{},{},{}".format(x,y,direction) not in visited):

        if map[y][x] == "#" or (obstruction is not None and x == obstruction[0] and y == obstruction[1]):
            direction = turn(direction)
            x,y = prev_x, prev_y
        else:
            visited.add("{},{},{}".format(x,y,direction))
            prev_x, prev_y = x, y

        x, y = move(direction, x, y)

    if inRange(map, x, y):
        path_type = 1

    return path_type


def printMap(map, obstruction=None):

    for y in range(len(map)):
        for x in range(len(map[0])):
            if obstruction is not None and obstruction[0] == x and obstruction[1] == y:
                print("0", end="")
            else:
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

def getStartPosition(map):
    
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == "^":
                return x,y

    return -1,-1


if __name__ == "__main__":
    main()
