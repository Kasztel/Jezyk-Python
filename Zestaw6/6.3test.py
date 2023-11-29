# !/usr/bin/env/python
# coding = utf-8

from points import Point
from rectangle import Rectangle
import unittest


class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.A = Rectangle(2, 0, 3, 2)
        self.B = Rectangle(2, 2, -0.9, 4.01)
        self.C = Rectangle(3, 2, 2, 0)

    def testStr(self):
        self.assertEqual(str(self.A), "[(2, 0), (3, 2)]")
        self.assertEqual(str(self.B), "[(2, 2), (-0.9, 4.01)]")

    def testRepr(self):
        self.assertEqual(repr(self.A), "Rectangle(2, 0, 3, 2)")
        self.assertEqual(repr(self.B), "Rectangle(2, 2, -0.9, 4.01)")

    def testEqual(self):
        self.assertEqual(self.A == self.A, True)
        self.assertEqual(self.A == self.C, True)
        self.assertEqual(self.A == self.B, False)

    def testNotEqual(self):
        self.assertEqual(self.A != self.A, False)
        self.assertEqual(self.A != self.B, True)

    def testCenter(self):
        self.assertEqual(self.A.center(), Point(2.5, 1))
        self.assertEqual(self.C.center(), Point(2.5, 1))

    def testArea(self):
        self.assertEqual(self.A.area(), 5)
        self.assertEqual(self.B.area(), 5.2501)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
