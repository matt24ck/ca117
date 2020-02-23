#!/usr/bin/env python3

import sys

nums = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
}

lines = sys.stdin.readlines()

for line in lines:
    line = line.strip().split()
    a = []
    i = 0
    while i < len(line):
        a.append(nums[line[i]])
        i += 1
    print(" ".join(a))
