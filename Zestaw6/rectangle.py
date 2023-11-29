from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return "[" + str(self.pt1) + ", " + str(self.pt2) + "]"

    def __repr__(self):  # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle(" + str(self.pt1.x) + ", " + str(self.pt1.y) + ", " + str(self.pt2.x) + ", " + str(
            self.pt2.y) + ")"

    def __eq__(self, other):  # obsługa rect1 == rect2
        if self.pt1 != other.pt1 and self.pt1 != other.pt2:
            return False
        if self.pt2 != other.pt1 and self.pt2 != other.pt2:
            return False
        return True

    def __ne__(self, other):  # obsługa rect1 != rect2
        return not self == other

    def center(self):  # zwraca środek prostokąta
        vCenter = self.pt1 + self.pt2
        return Point(round(vCenter.x) / 2, round(vCenter.y) / 2)

    def area(self):  # pole powierzchni
        a = abs(self.pt1.x - self.pt2.x)
        b = abs(self.pt1.y - self.pt2.y)

        return a * b

    def move(self, x, y):  # przesunięcie o (x, y)
        toMove = Point(x, y)

        return Rectangle(self.pt1 + toMove, self.pt2 + toMove)
    

