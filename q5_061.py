 #!/usr/bin/env python3

import sys

def get_total(l):
    total = 0
    for i in l:
        total += int(i)
    return(total)
def sorter(t):
    return t[-1]
def main():
    d = {}
    dq = []
    maxLen1 = 0
    maxLen2 = 0
    lines = sys.stdin.readlines()
    for line in lines:
        total = 0
        line = line.strip().split()
        club, res = [line[:-5], line[-5:]]
        club = " ".join(club)
        try:
            for i in res:
                total += int(i)
            d[club] = total
            if len(club) > maxLen1:
                maxLen1 = len(club)
            if len(str(total)) > maxLen2:
                maxLen2 = len(str(total))
        except ValueError:
            dq.append(club)
    for q, w in sorted(d.items(), key=sorter, reverse=True):
        print("{:>{}}: {:>{}} points".format(q, maxLen1, w, maxLen2))
    print("Disqualified:")
    for j in dq:
        print(j)
main()
