import pytest
from geograph import Node
from geograph import Line
from random import choice


def test_line():
    n1 = Node(1, 0)
    l1 = Line(n1, n1)
    assert l1 is None


def test_line_eq():
    n1 = Node(1.0, 0.0)
    n2 = Node(0.0, 1.0)
    l1 = Line(n1, n2)
    l2 = Line(n2, n1)
    assert l1 == l2


def test_edgeset():
    nodes = [Node(0, 0), Node(0, 1), Node(1, 0), Node(1, 1)]
    vertices = set()
    for i in range(1000):
        edge = Line(choice(nodes), choice(nodes))
        if edge:
            vertices.add(edge)
    assert len(vertices) == 6


def test_line_iter():
    n1 = Node(5, 6)
    n2 = Node(-1, 433)
    e = Line(n1, n2)
    coords = list(e)
    assert all([ci == cj for ci, cj in zip(e, [5.0, 6.0, -1.0, 433.0])])


def test_line_set_width():
    n0 = Node(0, 0)
    n1 = Node(1, 0)
    l = Line(n0, n1)

    l.set_length(10, ref_pt="start")
    assert pytest.approx(10.0) == l.length
    assert pytest.approx(10.0) == l.end.x 

    l.set_length(20, ref_pt="end")
    assert pytest.approx(20.0) == l.length
    assert pytest.approx(10.0) == l.end.x 
    assert pytest.approx(-10.0) == l.start.x 

    l.set_length(1, ref_pt="center")
    assert pytest.approx(1.0) == l.length
    assert pytest.approx(-0.5) == l.start.x 

    with pytest.raises(ValueError) as err:
        l.set_length(50, ref_pt="false_reference")

    with pytest.raises(AssertionError) as err:
        l.set_length(-50)
    
    assert pytest.approx(0.5) == l.end.x 


def test_line_move():
    
    n0 = Node(0, 0)
    n1 = Node(1, 0)
    l = Line(n0, n1)

    l.move(xn=1.0, yn=1.0, ref_pt='start')
    assert pytest.approx([1.0, 1.0]) == list(l.start)
    assert pytest.approx([2.0, 1.0]) == list(l.end)
    assert pytest.approx(1.0) == l.length

    l.move(xn=0, yn=0)
    assert pytest.approx([0.0, 0.0]) == list(l.center_point)
    assert pytest.approx([-0.5, 0.0]) == list(l.start)
    assert pytest.approx([0.5, 0.0]) == list(l.end)
    assert pytest.approx(1.0) == l.length

def test_line_rotate():
    n0 = Node(1, 0)
    n1 = Node(2, 0)
    l = Line(n0, n1)

    l.rotate(90)
    assert pytest.approx([0.0, 1.0]) == list(l.start)
    assert pytest.approx([0.0, 2.0]) == list(l.end)
