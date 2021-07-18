from nodegraph import Node
from nodegraph import Line
import pytest
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
    nodes = list(e)
    assert nodes[0] == n1
    assert nodes[1] == n2
