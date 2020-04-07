#!/usr/bin/env python3

def count_letters(s):
    if s == "":
        return 0
    elif s != "":
        count = 1
        s = s[1:]
        count += count_letters(s)
    return count

if __name__ == "__main__":
    len = None
    print(count_letters('cat'))
    print(count_letters('catastrophe'))
    print(count_letters(''))
