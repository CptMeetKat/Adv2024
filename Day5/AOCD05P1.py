#!/usr/bin/python3

import sys


def main():
    if len(sys.argv) < 2:
        print("No input file provided")
        sys.exit(1)
    rules_raw, print_orders = parseInput(sys.argv[1])
    rules = parseRules(rules_raw)
    
    result = 0
    for line in print_orders:
        pages = line.split(",")
        isCorrect = isPrintOrderCorrect(pages, rules)
        if isCorrect:
            result += getMiddleValue(pages)

    print("Result: {}".format(result))
 
def isPrintOrderCorrect(pages, rules):
    
    pages_length = len(pages)
    for i in range(pages_length-1):
        valueI = int(pages[i])
        for j in range(i+1, pages_length):
            valueJ = int(pages[j])

            if valueI in rules: #rules {after: before}
                if valueJ in rules[valueI]:
                    return False
    
    return True
            
def parseRules(rules_raw):
    rules = {}
    for r in rules_raw:
        rule = r.split("|")
        before = int(rule[0])
        after = int(rule[1])

        if after in rules:
            rules[after].add(before)
        else:
            rules[after] = {before}
    return rules
            
def getMiddleValue(pages):
    length = len(pages)
    middle_value = int(pages[    (int((length/2)))] )
    return middle_value


def parseInput(filename):
    sectionA = []
    sectionB = []

    buffer = []
    with open(filename, 'r') as file:
        
        for l in file:
            line = l.strip()
            if line == "":
                sectionA = buffer.copy()
                buffer = []
            else:
                buffer.append(line)
    sectionB = buffer.copy()

    return sectionA, sectionB

if __name__ == "__main__":
    main()
