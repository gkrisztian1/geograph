from nodegraph import Node
from random import shuffle
import operator
from copy import copy
import pytest


def test_node_bool():
    n1 = Node(0, 0)
    assert n1 is not None


def test_node_copytest():
    n1 = Node(5, 2)
    n2 = copy(n1)
    assert id(n1) != id(n2)
    assert n1.name != n2.name
    assert n1 is not n2


def test_node_eq():

    n1 = Node(1, 0)
    n2 = Node(1, 0)
    assert n1 == n2


def test_node_neq():

    n1 = Node(1.0, 0)
    n2 = Node(0, 1.0)
    assert (n1 == n2) is False
    assert n1 != n2


def test_node_add():
    """
    1. Node + scalar
    2. Node + iterable
    2.1 Node + invalid iterable
    3. Node1 + Node2

    4. scalar + Node
    5. iterable + Node
    6. Node2 + Node1

    7. Node += scalar
    8. Node += iterable
    8.1 Node + invalid iterable
    9. Node1 += Node2

    10. Node + invalid
    11. invalid + Node
    12. Node += invalid
    """

    # 1. Node + scalar
    n0 = Node(0, 0)
    n1 = n0 + 5
    assert n1 == Node(5, 5)

    # 2. Node + iterable
    n0 = Node(0, 0)
    n1 = n0 + (5, 5, 5, 5)
    assert n1 == Node(5, 5)

    # 2.1 Node + invalid iterable
    # TODO: This should raise an error or fall back to scalar addition
    # n0 = Node(1, 1)
    # n1 = n0 + (5)
    # assert n1 == Node(6, 6)

    # 3. Node1 + Node2
    n0 = Node(-10, 50)
    n1 = Node(10, 100)
    assert n0 + n1 == Node(0, 150)

    # 4. scalar + Node
    n0 = Node(0, 0)
    n1 = 5 + n0
    assert n1 == Node(5, 5)

    # 5. iterable + Node
    n0 = Node(0, 0)
    n1 = (5, 5, 5, 5) + n0
    assert n1 == Node(5, 5)

    # 6. Node2 + Node1
    n0 = Node(50, -1)
    n1 = Node(-50, 1)
    assert n1 + n0 == Node(0, 0)

    # 7. Node += scalar
    n0 = Node(0, 0)
    n0 += 601
    assert n0 == Node(601, 601)

    # 8. Node += iterable
    n0 = Node(0, 0)
    n0 += (5, 6, 7, 8, 9, 10)
    assert n0 == Node(5, 6)

    # 9. Node1 += Node2
    n0 = Node(-10, 10)
    n1 = Node(10, -10)
    n0 += n1
    assert n0 == Node(0, 0)

    # 10. Node + invalid
    # 11. invalid + Node
    # 12. Node += invalid


def test_node_sub():
    """
    1. Node - scalar
    2. Node - iterable
    2.1 Node - invalid iterable
    3. Node1 - Node2

    4. scalar - Node
    5. iterable - Node
    6. Node2 - Node1

    7. Node -= scalar
    8. Node -= iterable
    8.1 Node - invalid iterable
    9. Node1 -= Node2

    10. Node - invalid
    11. invalid - Node
    12. Node -= invalid
    """

    # 1. Node - scalar
    n0 = Node(0, 0)
    n1 = n0 - 5
    assert n1 == Node(-5, -5)

    # 2. Node - iterable
    n0 = Node(0, 0)
    n1 = n0 - (5, 5, 5, 5)
    assert n1 == Node(-5, -5)

    # 2.1 Node - invalid iterable
    # TODO: This should raise an error or fall back to scalar addition
    # n0 = Node(1, 1)
    # n1 = n0 - (5)
    # assert n1 == Node(6, 6)

    # 3. Node1 - Node2
    n0 = Node(-10, 50)
    n1 = Node(10, 100)
    assert n0 - n1 == Node(-20, -50)

    # 4. scalar - Node
    with pytest.raises(ValueError, match="You cannot subtract a Node from a number."):
        n0 = Node(0, 0)
        n1 = 5 - n0
        assert n1 == Node(5, 5)

    # 5. iterable - Node
    n0 = Node(0, 0)
    n1 = (5, 5, 5, 5) - n0
    assert n1 == Node(5, 5)

    # 6. Node2 - Node1
    n0 = Node(50, -1)
    n1 = Node(-50, 1)
    assert n1 + n0 == Node(0, 0)

    # 7. Node -= scalar
    n0 = Node(0, 0)
    n0 += 601
    assert n0 == Node(601, 601)

    # 8. Node -= iterable
    n0 = Node(0, 0)
    n0 += (5, 6, 7, 8, 9, 10)
    assert n0 == Node(5, 6)

    # 9. Node1 -= Node2
    n0 = Node(-10, 10)
    n1 = Node(10, -10)
    n0 -= n1
    assert n0 == Node(-20, 20)

    # 10. Node + invalid
    # 11. invalid + Node
    # 12. Node += invalid


def test_mul():

    # scalar multiplication
    n1 = Node(2, 4)
    n2 = Node(-4, 3)

    assert (n1 * 5) == Node(10, 20)
    assert (5 * n1) == Node(10, 20)

    # dot product
    assert n1 * n2 == 4.0

    # cross product
    # v1x * v2y - v1y * v2x
    assert n1 @ n2 == (2 * 3) - (4 * -4)


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

    nodes = [a, b, c, d, e, f, g, h, i]
    shuffle(nodes)
    nodes.sort()

    reference_nodes = [e, d, b, f, h, a, c, i, g]
    assert all(map(operator.eq, nodes, reference_nodes))


def test_attribute_error():
    n = Node(5, 6)
    with pytest.raises(AttributeError):
        print(n.j)
