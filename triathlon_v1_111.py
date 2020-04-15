#!/usr/bin/env python3

class Triathlon(object):
    def __init__(self, athletes={}):
        self.athletes = athletes

    def add(self, inst):
        self.athletes[inst.tid] = inst

    def remove(self, i):
        del self.athletes[i]

    def lookup(self, i):
        try:
            return self.athletes[i]
        except:
            return None

class Triathlete(Triathlon):
    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        return "Name: {}\nID: {}".format(self.name, self.tid)

def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)

    tn.add(t1)
    tn.add(t2)

    t = tn.lookup(21)
    print(isinstance(t, Triathlete))
    print(t.name == 'Ian Brown')
    print(t.tid == 21)

    tn.remove(21)
    t = tn.lookup(21)
    print(t is None)

if __name__ == '__main__':
    main()
