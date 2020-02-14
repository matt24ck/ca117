#!/usr/bin/env python

import sys

text = sys.stdin.read()
arg = sys.argv[1]
with open(arg) as f:
    toBan = f.readlines()
i = 0
banned = []
while i < len(toBan):
    banned.append(toBan[i].rstrip())
    i += 1
j = 0
while j < len(banned):
    i = 0
    while i < len(text):
        if text[i:i + len(banned[j])] == banned[j]:
            text = text.replace(text[i:i + len(banned[j])], len(banned[j]) * '@', 1)
        i += 1
    j += 1
sys.stdout.write(text)
