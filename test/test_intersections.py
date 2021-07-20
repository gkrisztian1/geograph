from nodegraph import Node, Line
from nodegraph import Geometry


def get_line(x0, y0, x1, y1):
    return Line(Node(x0, y0), Node(x1, y1))


def get_ref_line():
    return get_line(0, 0, 10, 0)


def test_zero_intersections():
    e0 = get_ref_line()

    e1 = get_line(0, 1, 5, 1)
    e2 = get_line(3, 1, 4, 9)
    e3 = get_line(1, 5, 10, 6)
    e4 = get_line(5, 1, 5, 10)

    assert len(Geometry.get_intersections(*e0, *e1)) == 0
    assert len(Geometry.get_intersections(*e0, *e2)) == 0
    assert len(Geometry.get_intersections(*e0, *e3)) == 0
    assert len(Geometry.get_intersections(*e0, *e4)) == 0


def test_1_intersection():
    e0 = get_ref_line()

    e1 = get_line(10, 0, 15, 4)
    e2 = get_line(10, 0, 15, 0)
    e3 = get_line(5, 0, 5, 10)
    e4 = get_line(5, -1, 6, 4)

    assert len(Geometry.get_intersections(*e0, *e1)) == 1
    assert len(Geometry.get_intersections(*e0, *e2)) == 1
    assert len(Geometry.get_intersections(*e0, *e3)) == 1
    assert len(Geometry.get_intersections(*e0, *e4)) == 1


def test_2_intersections():
    e0 = get_ref_line()

    e1 = get_line(8, 0, 20, 0)
    e2 = get_line(3, 0, 8, 0)
    e3 = get_line(7, 0, 10, 0)
    e4 = get_ref_line()

    assert len(Geometry.get_intersections(*e0, *e1)) == 2
    assert len(Geometry.get_intersections(*e0, *e2)) == 2
    assert len(Geometry.get_intersections(*e0, *e3)) == 2
    assert len(Geometry.get_intersections(*e0, *e4)) == 2
