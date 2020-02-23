#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

contacts = {}
for line in lines:
    line = line.strip().split()
    contacts[line[0]] = [line[1], line[2]]
lines = sys.stdin.readlines()
for line in lines:
    line = line.strip()
    if line in contacts:
        number = "Phone: " + contacts[line][0] + '\n'
        email = "Email: " + contacts[line][1] + '\n'
    else:
        number = "No such contact\n"
        email = ''
    sys.stdout.write("Name: {}\n".format(line))
    sys.stdout.write("{}".format(number))
    sys.stdout.write("{}".format(email))
