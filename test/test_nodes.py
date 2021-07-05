from nodegraph import Node
from random import shuffle
import operator

def test_node_eq():

    n1 = Node(1, 0)
    n2 = Node(1, 0)
    assert n1==n2

def test_node_neq():

    n1 = Node(1.0, 0)
    n2 = Node(0, 1.0)
    assert n1 != n2


def test_sort_nodes():
    a = Node(1, 1)
    b = Node(0, 1)
    c = Node(-1, 1)
    d = Node(1, 0)
    e = Node(0, 0)
    f = Node(-1, 0)
    g = Node(1, -1)
    h = Node(0, -1)
    i = Node(-1, -1)

    nodes  = [a, b, c, d, e, f, g, h, i]
    shuffle(nodes)
    reference_nodes = [e, d, b, f, h, a, c, i, g]
    nodes.sort()
    assert all(map(operator.eq, nodes, reference_nodes))
