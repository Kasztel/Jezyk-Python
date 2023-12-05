from points import Point
import math


class Circle:
    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        return "Circle(" + str(self.pt.x) + ", " + str(self.pt.y) + ", " + str(self.radius) + ")"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return math.pi * (self.radius ** 2)

    def move(self, x, y):
        tomove = Point(x, y)

        return Circle(self.pt.x + tomove.x, self.pt.y + tomove.y, self.radius)

    def cover(self, other):
        r1 = self.radius
        r2 = other.radius
        x1 = self.pt.x
        y1 = self.pt.y
        x2 = other.pt.x
        y2 = other.pt.y

        if r1 > r2:
            r1, r2 = r2, r1
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        if (distance + r1) <= r2:
            return Circle(x2, y2, r2)
        else:
            enclosingRadius = (distance + r1 + r2) / 2
            theta = 1 / 2 + (r2 - r1) / (2 * distance)
            centerX = (1 - theta) * x1 + theta * x2
            centerY = (1 - theta) * y1 + theta * y2
            return Circle(centerX, centerY, enclosingRadius)
