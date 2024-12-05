#!/usr/bin/python3

import sys


def main():
    if len(sys.argv) < 2:
        print("No input file provided")
        sys.exit(1)
    rules_raw, print_orders = parseInput(sys.argv[1])
    rules = parseRules(rules_raw)
    
    incorrect_lines = []
    result = 0
    for line in print_orders:
        pages = line.split(",")
        isCorrect = isPrintOrderCorrect(pages, rules)
        if not isCorrect:
            incorrect_lines.append(pages)

   
    for incorrect in incorrect_lines:
        number_list = list(map(asNumbers, incorrect))
        fixed = fix_incorrect(number_list, rules)
        result += getMiddleValue(fixed)

    print("Result: {}".format(result))

def asNumbers(x):
    return int(x)

def fix_incorrect(numbers, rules):
    length = len(numbers)
    for i in range(length-1):
        for j in range(i+1, length):
            if numbers[j] in rules:
                if numbers[i] in rules[numbers[j]]:
                    t = numbers[j]
                    numbers[j] = numbers[i]
                    numbers[i] = t

    return numbers

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
