#!/usr/bin/python3

import sys

def main():
    if len(sys.argv) < 2:
        print("No input file provided")
        sys.exit(1)

    run(sys.argv[1])
    
def run(filename):
    data = getData(filename)
    diskmap = [int(i) for i in data]

    result = 0
    length = len(diskmap)
    next_free = 0

    right = length-1
    for i in range(length):
        if i % 2 == 0:
            while diskmap[i] > 0:
                file_id = int(i/2)
                result += file_id * next_free 
                next_free+=1
                diskmap[i]-=1
        else:
            while diskmap[i] > 0 and i < right:
                right_file_id = int(right/2)
                result += right_file_id * next_free
                diskmap[i]-=1
                diskmap[right]-=1
                next_free+=1

                while diskmap[right] <= 0:
                    right -=2
        if i >= right: 
            break

    print("Result:", result)


def render(diskmap):
    print("Render: ", end="")
    for i in range(len(diskmap)):
        for _ in range(diskmap[i]):
            if i % 2 == 0:
                print(int(i/2), end="")
            else:
                print(".", end="")

    print()
               

def getData(filename):
    lines = []
    with open(filename, 'r') as file:
        lines += list(file.read().strip())

    return lines

if __name__ == "__main__":
    main()
