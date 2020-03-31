#!/usr/bin/env python3

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

class Shape(object):
    def __init__(self, points):
        self.points = points

    def sides(self):
        if len(self.points) == 3:
            return [self.points[0].distance(self.points[1]), self.points[1].distance(self.points[2]), self.points[2].distance(self.points[0])]
        else:
            return [self.points[0].distance(self.points[1]), self.points[1].distance(self.points[2]), self.points[2].distance(self.points[3]), self.points[3].distance(self.points[0])]

    def perimeter(self):
        return sum(self.sides())

class Triangle(Shape):
    def area(self):
        s = sum(self.sides()) / 2
        return (s * (s - self.sides()[0]) * (s - self.sides()[1]) * (s - self.sides()[2])) ** 0.5

class Square(Shape):
    def area(self):
        return self.sides()[1] ** 2

def main():

    t1 = Triangle([Point(0,0), Point(3,4), Point(6, 0)])
    print(t1.sides())
    print(t1.perimeter())
    print(t1.area())

    t2 = Triangle([Point(0,0), Point(4,0), Point(4, 3)])
    print(t2.sides())
    print(t2.perimeter())
    print(t2.area())

    s1 = Square([Point(0,0), Point(5,0), Point(5,5), Point(0,5)])
    print(s1.sides())
    print(s1.perimeter())
    print(s1.area())

if __name__ == '__main__':
    main()
