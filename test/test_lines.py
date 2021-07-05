from nodegraph import Node
from nodegraph import Line
import pytest


def test_line_eq():
    n1 = Node(1.0, 0.0)
    n2 = Node(0.0, 1.0)
    l1 = Line(n1, n2)
    l2 = Line(n2, n1)
    assert l1 == l2
