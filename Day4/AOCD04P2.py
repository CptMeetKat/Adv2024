#!/usr/bin/python3

import sys

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


    for y in range(y_max-2):
        for x in range(x_max-2):
            result += matchXMAS(data, x, y)
    
    print("Result: {}".format(result))


def matchXMAS(block, x_start, y_start):
    stencil = [['M', '.', 'M'], ['.', 'A', '.'], ['S', '.', 'S']]
    
    for _ in range(4):
        match = 1

        for x in range(0, 3):
            for y in range(0, 3):
                target = block[y_start+y][x_start+x]
                s_target = stencil[y][x]
                if s_target == ".":
                    continue
                elif target != s_target:
                    match = 0 


        if match == 1:
            return 1
        stencil = rotate(stencil)
            
    return 0

def rotate(square):
    template = [  ['','',''], ['','',''],['','','']  ]
    for y in range(3):
        for x in range(3):
            template[y][x] = square[3-x-1][y] #MAGIC 2d rotation around grid
    return template


if __name__ == "__main__":
    main()
