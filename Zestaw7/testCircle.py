# !/usr/bin/env/python
# coding = utf-8

import math
from circle import Circle
import unittest


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.A = Circle(0, 0, 5)
        self.B = Circle(2, 3, 1)
        self.C = Circle(2, 2, 1)

    def testException(self):
        try:
            temp = Circle(0, 0, -5)
        except ValueError as expect:
            self.assertEqual(expect.args[0], "promień ujemny")

    def testRepr(self):
        self.assertEqual(str(self.A), "Circle(0, 0, 5)")
        self.assertEqual(str(self.B), "Circle(2, 3, 1)")

    def testEqual(self):
        self.assertEqual(self.A == self.A, True)
        self.assertEqual(self.A == self.B, False)

    def testNEqual(self):
        self.assertEqual(self.A != self.A, False)
        self.assertEqual(self.A != self.B, True)

    def testArea(self):
        self.assertEqual(self.A.area(), 25 * math.pi)
        self.assertEqual(self.B.area(), math.pi)

    def testMove(self):
        self.assertEqual(self.A.move(2, 2), Circle(2, 2, 5))
        self.assertEqual(self.B.move(-2, -3), Circle(0, 0, 1))

    def testCover(self):
        self.assertEqual(self.A.cover(self.B), Circle(0, 0, 5))
        self.assertEqual(self.B.cover(self.C), Circle(2,2.5,1.5))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
