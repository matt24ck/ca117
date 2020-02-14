#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
myList = []
for line in lines:
    myList.append(line.strip())
def shortest_all_vowels(a):
    shortestlen = 10000000
    shortest = ""
    for line in a:
        if len(line) < shortestlen:
            i = 0
            count = 0
            vowels = "aeiou"
            while i < len(line):
                if line[i] in vowels:
                    vowels = vowels.replace(line[i], "", 1)
                    count += 1
                i += 1
            if count == 5:
                shortest = line
                shortestlen = len(line)
    return shortest
def four_as(a):
    new_list = []
    for line in a:
        i = 0
        count = 0
        while i < len(line):
            if line[i].lower() == "a":
                count += 1
            i += 1
        if count == 4:
            new_list.append(line)
    return new_list

def two_plus_qs(a):
    new_list = []
    for line in a:
        i = 0
        count = 0
        while i < len(line):
            if line[i].lower() == "q":
                count += 1
            i += 1
        if count >= 2:
            new_list.append(line)
    return new_list
def anagram_of_angle(a):
    new_list = []
    for line in a:
        if not line.lower() == "angle" and sorted(line.lower()) == sorted("angle"):
            new_list.append(line)
    return new_list
def most_es(a):
    new_list = []
    ecount = 0
    for line in a:
        count = 0
        i = 0
        while i < len(line):
            if line[i] == "e":
                count += 1
            i += 1
        if count > ecount:
            ecount = count
    for line in a:
        count = 0
        i = 0
        while i < len(line):
            if line[i] == "e":
                count += 1
            i += 1
        if count == ecount:
            new_list.append(line)
    return new_list
def ends_in_iary(s):
    return len(s) > 3 and s[len(s) - 4:] == "iary"

print("Words containing 17 letters: {}".format([i for i in myList if len(i) == 17]))
print("Words containing 18+ letters: {}".format([i for i in myList if len(i) >= 18]))
print("Shortest word containing all vowels: {}".format(shortest_all_vowels(myList)))
print("Words with 4 a's: {}".format(four_as(myList)))
print("Words with 2+ q's: {}".format(two_plus_qs(myList)))
print("Words containing cie: {}".format([i for i in myList if "cie" in i.lower()]))
print("Anagrams of angle: {}".format(anagram_of_angle(myList)))
print("Words ending in iary: {}".format(len([i for i in myList if ends_in_iary(i)])))
print("Words with most e's: {}".format(most_es(myList)))
