# !/usr/bin/env/python
# coding = utf-8

from math import sqrt
import unittest
from points import Point


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.zero = Point(0, 0)

    def testStr(self):
        self.assertEqual(str(Point(12, 3)), "(12, 3)")
        self.assertEqual(str(Point(2.7, 8.88)), "(2.7, 8.88)")

    def testRepr(self):
        self.assertEqual(repr(Point(12, 3)), "Point(12, 3)")
        self.assertEqual(repr(Point(2.7, 8.88)), "Point(2.7, 8.88)")

    def testEqual(self):
        self.assertEqual(Point(12, 3) == Point(12, 3), True)
        self.assertEqual(Point(2.7, 8.88) == Point(12, 3), False)

    def testNotEqual(self):
        self.assertEqual(Point(12, 3) != Point(12, 3), False)
        self.assertEqual(Point(2.7, 8.88) != Point(12, 3), True)

    def testAdd(self):
        self.assertEqual(Point(4, 1.1) + Point(2, 15), Point(6, 16.1))
        self.assertEqual(Point(5, 5) + Point(5, 5), Point(10, 10))

    def testSub(self):
        self.assertEqual(Point(4, 1.1) - Point(2, 15), Point(2, -13.9))
        self.assertEqual(Point(5, 5) - Point(5, 5), Point(0, 0))

    def testMul(self):
        self.assertEqual(Point(4, 1.1) * Point(2, 15), 24.5)
        self.assertEqual(Point(5, 5) * Point(5, 5), 50)

    def testCross(self):
        self.assertEqual(Point(4, 5).cross(Point(2, 15)), 50)
        self.assertEqual(Point(5, 5).cross(Point(5, 5)), 0)

    def testLength(self):
        self.assertEqual(Point(5, 12).length(), 13)
        self.assertEqual(Point(2, 3).length(), sqrt(13))

    def testHash(self):
        self.assertEqual(hash(Point(12, 2.3)), hash((12, 2.3)))

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
