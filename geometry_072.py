#!/usr/bin/env python3

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def distance(self, point):
        dist = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        return dist

    def __str__(self):
        return '({:.1f}, {:.1f})'.format(self.x, self.y)

class Segment:
    def __init__(self, p1, p2):
        self.p1x = p1.x
        self.p2x = p2.x
        self.p1y = p1.y
        self.p2y = p2.y

    def midpoint(self):
       out = Point()
       out.x = (self.p1x + self.p2x) / 2
       out.y = (self.p1y + self.p2y) / 2
       return out

    def length(self):
       out = ((self.p1x - self.p2x) ** 2 + (self.p1y - self.p2y) ** 2) ** 0.5
       return out

class Circle:
    def __init__(self, point, radius):
        self.pointx = point.x
        self.pointy = point.y
        self.radius = radius

    def overlaps(self, circle):
       tf = ((self.pointx - circle.pointx) ** 2 + (self.pointy - circle.pointy) ** 2) ** 0.5 < (self.radius + circle.radius)
       return tf

if __name__ == "__main__":
    p1 = Point(3, 4)
    s1 = Segment(Point(), p1)
    mid = s1.midpoint()
    c1 = Circle(p1, 5)
    c2 = Circle(p1, 2)
    print(c1.overlaps(c2))
    print(mid)
