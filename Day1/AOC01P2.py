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
    b_freq={}
    for l in data.split():
        value=int(l)
        if column == 0:
            a.append(value)
            column = 1
        else:
            if value in b_freq:
                b_freq[value]+=1
            else:
                b_freq[value]=1
            column = 0

    a.sort()

    for i in a:
        if i in b_freq:
            simlarity_score = b_freq[i] * i
            result+=simlarity_score

    print("Result is: {}".format(result))


if __name__ == "__main__":
    main()





