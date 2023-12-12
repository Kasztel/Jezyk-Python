from points import Point
import math


class Circle:
    def __init__(self, *args):
        if len(args) == 3:
            if args[2] < 0:
                raise ValueError("promień ujemny")
            self.pt = Point(args[0], args[1])
            self.radius = args[2]
        elif len(args) == 6:
            self.pt1 = Point(args[0], args[1])
            self.pt2 = Point(args[2], args[3])
            self.pt3 = Point(args[4], args[5])
        else:
            raise ValueError("Incorrect ammount of arguments")

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

    def from_points(points):
        circ = Circle(0, 0, 0, 0, 0, 0)
        circ.pt1 = points[0]
        circ.pt2 = points[1]
        circ.pt3 = points[2]

        x1 = circ.pt1.x
        y1 = circ.pt1.y
        x2 = circ.pt2.x
        y2 = circ.pt2.y
        x3 = circ.pt3.x
        y3 = circ.pt3.y

        x12 = x1 - x2
        x13 = x1 - x3
        y12 = y1 - y2
        y13 = y1 - y3
        y31 = y3 - y1
        y21 = y2 - y1
        x31 = x3 - x1
        x21 = x2 - x1

        sx13 = pow(x1, 2) - pow(x3, 2)
        sy13 = pow(y1, 2) - pow(y3, 2)

        sx21 = pow(x2, 2) - pow(x1, 2)
        sy21 = pow(y2, 2) - pow(y1, 2)

        f = (((sx13) * (x12) + (sy13) *
              (x12) + (sx21) * (x13) +
              (sy21) * (x13)) // (2 *
                                  ((y31) * (x12) - (y21) * (x13))))

        g = (((sx13) * (y12) + (sy13) * (y12) +
              (sx21) * (y13) + (sy21) * (y13)) //
             (2 * ((x31) * (y12) - (x21) * (y13))))

        c = (-pow(x1, 2) - pow(y1, 2) -
             2 * g * x1 - 2 * f * y1)

        h = -g
        k = -f
        sqr_of_r = h * h + k * k - c

        r = round(math.sqrt(sqr_of_r), 5)

        return Circle(h, k, r)

    @property
    def top(self):
        return self.pt.y + self.radius

    @property
    def left(self):
        return self.pt.x - self.radius

    @property
    def bottom(self):
        return self.pt.y - self.radius

    @property
    def right(self):
        return self.pt.x + self.radius

    @property
    def width(self):
        return self.right - self.left

    @property
    def height(self):
        return self.top - self.bottom

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)