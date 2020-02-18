#!/usr/bin/env python3

import sys

vowelCount = {
    "e": 0,
    "a": 0,
    "i": 0,
    "o": 0,
    "u": 0,
}
text = sys.stdin.read()
i = 0
while i < len(text):
    if text[i].lower() in vowelCount:
        vowelCount[text[i].lower()] += 1
    i += 1
tups = []
for a, b in vowelCount.items():
    tup = a, b
    tups.append(tup)
tups.sort(key=lambda x: x[1], reverse=True)
blen = len(str(tups[0][1]))
for a, b in tups:
    print("{} : {:>{:d}d}".format(a, b, blen))
