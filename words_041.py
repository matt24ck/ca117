#!/usr/bin/env python3

import sys
from string import punctuation

text = sys.stdin.read()
myDic = {}
i = 0
while i < len(text):
    if not text[i].isalpha() and not text[i] == "'":
        text = text.replace(text[i], " ")
    i += 1
words = text.lower().split()
for word in words:
    myDic[word] = 0
for word in words:
    myDic[word] += 1
for i in sorted(myDic):
    print("{} : {}".format(i, myDic[i]))
