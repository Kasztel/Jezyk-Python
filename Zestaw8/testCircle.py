# !/usr/bin/env/python
# coding = utf-8
import math

from points import Point
from circle import Circle
import pytest


@pytest.fixture
def circle():
    return Circle(2, -2, 4)


def test_from_points(circle):
    points = [Point(-2, -2), Point(2, -6), Point(6, -2)]
    circ = Circle.from_points(points)
    assert circle == circ


def test_top(circle):
    assert circle.top == 2


def test_left(circle):
    assert circle.left == -2


def test_bottom(circle):
    assert circle.bottom == -6


def test_right(circle):
    assert circle.right == 6


def test_width(circle):
    assert circle.width == 8


def test_height(circle):
    assert circle.height == 8


def test_top_left(circle):
    assert circle.topleft == Point(-2, 2)


def test_top_right(circle):
    assert circle.topright == Point(6, 2)


def test_bottom_left(circle):
    assert circle.bottomleft == Point(-2, -6)


def test_bottom_right(circle):
    assert circle.bottomright == Point(6, -6)


def test_area(circle):
    assert circle.area() == math.pi * 4 * 4


def test_move(circle):
    circ = circle.move(2, 2)
    assert circ == Circle(4, 0, 4)


def test_cover(circle):
    circ = Circle(0, 0, 1)
    assert Circle.cover(circle, circ) == Circle(2, -2, 4)


if __name__ == '__main__':
    pytest.main()
