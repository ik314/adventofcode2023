#!/usr/bin/env python3
import re

calib_file = open("../test/01.txt")

def part1(calib_file):
    running_total = 0
    for line in calib_file.readlines():
        numbers_only = re.sub('[a-zA-Z\\n]+', "", line)
        first_last_s = numbers_only[0] + numbers_only[-1]
        # print("{} ({})".format(first_last_s, numbers_only))

        first_last_int = int(first_last_s)
        running_total += first_last_int

    print("\n\nFinal Running Total: {}\n\n".format(running_total))
    return running_total

alpha_to_numerical = {"one": 1, "two": 2, "three": 3, "four": 4,
                          "five": 5, "six": 6, "seven": 7, "eight": 8,
                          "nine": 9} # perhaps there was a nicer way to do this
                                     # oh well.
def checkIfSpelledDigit(str):
    for key in alpha_to_numerical.keys():
        if key in str:
            return alpha_to_numerical[key]

    return False

def checkIfNumericalDigit(char):
    return char.isnumeric()

def part2(calib_file):
    running_total = 0
    # first parse, turn all "spelled out" digits into numbers

    for line in calib_file.readlines():
        # a wasteful algorithm, but itll work
        # from the left side
        line = line.strip('\n')
        for l in range(len(line)):
            c = line[l]
            subsec = line[0:l] + c
            check_digit = checkIfSpelledDigit(subsec)
            if checkIfNumericalDigit(c):
                l_digit = c
                break
            elif check_digit != False:
                l_digit = str(check_digit)
                break

        print("og:              ", line)
        print("l_digit:         ", l_digit)

        for r in reversed(range(len(line))):
            c = line[r]
            subsec = line[r:len(line)]
            # print("subsec:", subsec)
            check_digit = checkIfSpelledDigit(subsec)
            if checkIfNumericalDigit(c):
                r_digit = c
                break
            elif check_digit != False:
                r_digit = str(check_digit)
                break

        running_total += int(l_digit+r_digit)
        # STATS PER LINE
        print("r_digit:         ", r_digit)
        print("l+r_digit:       ", l_digit+r_digit)
        print("running_total:   ", running_total)
        print("=================")

    print("\n\nFinal Running Total: {}\n\n".format(running_total))
    return running_total

# both return a running total
# as well as print it out.
# part1(calib_file)
# part2(calib_file)
