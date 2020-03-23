#!/usr/bin/env python3

import sys
def count_lines(l):
    count = 0
    for i in l:
        count += 1
    return count
def len_words(l):
    return len(l[0].strip())
def sorting(l):
    return l.lower()
def main():
    a = []
    lines = sys.stdin.readlines()
    count = count_lines(lines)
    mylen = len_words(lines)
    i = 0
    while i < mylen:
        a.append("")
        i += 1
    j = 0
#    print(a)
    while j < mylen:
        for line in lines:
            line = line.strip()
            a[j] += line[j]
        j += 1
    a.sort(key=sorting)
    k = 0
    while k < count:
        out = ''
        for i in a:
            out += i[k]
        print(out)
        k += 1

#    print(count)
#    print(a)
if __name__ == "__main__":
    main()
