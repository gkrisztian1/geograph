from time import sleep
from nodegraph.utils import *
from io import StringIO
from contextlib import redirect_stdout
from nodegraph import Geometry
import sys


def test_timing():
    @timing
    def f():
        sleep(0.5)
        return 1

    with StringIO() as buf, redirect_stdout(buf):
        f()
        assert buf.getvalue().find("function: f took: 5") != -1
        assert buf.getvalue().find("e-01 sec.") != -1


def test_hex2name():

    assert hex2name("none") == "white"
    assert hex2name("#b22222") == "firebrick"


def test_bbox_intersection():
    r0 = (0, 0, 1, 1)

    # These rectangles share one edge with r0
    r_above = (0, 1, 1, 2)
    r_below = (0, -1, 1, 0)
    r_left = (-1, 0, 0, 1)
    r_right = (1, 0, 2, 1)

    assert Geometry.is_rectangle_intersect(r0, r_above) == True
    assert Geometry.is_rectangle_intersect(r0, r_below) == True
    assert Geometry.is_rectangle_intersect(r0, r_left) == True
    assert Geometry.is_rectangle_intersect(r0, r_right) == True

    # Intersection test
    r1 = (0.5, 0.5, 1.5, 1.5)
    assert Geometry.is_rectangle_intersect(r0, r1) == True

    # r0 contains r1
    r1 = (0.1, 0.1, 0.8, 0.9)
    assert Geometry.is_rectangle_intersect(r0, r1) == True

    # r0 does not intersects with r1
    r1 = (5, 50, 100, 200)
    assert Geometry.is_rectangle_intersect(r0, r1) == False
