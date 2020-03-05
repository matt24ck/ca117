#!/usr/bin/env python3

import sys

def find_rogue(s):
    d = {}
    s = s.split(" ")
    i = 0
    while i < len(s):
        if int(s[i]) not in d:
            d[int(s[i])] = 1
        else:
            d[int(s[i])] += 1
        i += 1
    for key in d:
        if d[key] == 1:
            return key

def main():
    lines = sys.stdin.readlines()
    for s in lines:
        print(find_rogue(s))
main()
