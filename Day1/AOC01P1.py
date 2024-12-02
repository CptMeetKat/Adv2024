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


    result = 0

    column=0
    a=[]
    b=[]
    for l in data.split():
        if column == 0:
            a.append(int(l))
            column = 1
        else:
            b.append(int(l))
            column = 0

    a.sort()
    b.sort()

    for i in range(len(a)):
        distance = a[i] - b[i]
        result+=abs(distance)

    print("Result is: {}".format(result))


if __name__ == "__main__":
    main()





