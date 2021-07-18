from nodegraph import NodeGraph, Node
from nodegraph import default_color
from itertools import permutations
from collections import Counter
from math import inf


def count_color(g: NodeGraph, color=default_color):
    """
    This utility function counts how many edges have a certain color.
    """

    return Counter([ei.color for ei in g.edges]).get(color, 0)


def test_graph_creation():
    g = NodeGraph()

    assert g.color == "none"
    assert g.rank == 0
    assert len(g.vertices) == 0
    assert len(g.edges) == 0
    assert g.bbox_xmin == inf
    assert g.bbox_ymin == inf
    assert g.bbox_xmax == -inf
    assert g.bbox_ymax == -inf


def test_bounding_box():
    g = NodeGraph()
    g.add_line_coords(0, -100, 30, 0)
    g.add_line_coords(30, 0, 0, 123)
    g.add_line_coords(0, 123, -654, 0)

    assert g.bbox_xmin == -654.0
    assert g.bbox_xmax == 30.0
    assert g.bbox_ymin == -100.0
    assert g.bbox_ymax == 123.0


def test_filter_duplicate_nodes():
    g = NodeGraph()
    n = Node(5, 6)
    for i in range(10):
        g.add_node(n)

    g.add_node_coords(5, 6)
    g.add_node_coords(10, 10)

    assert len(g.vertices) == 2


def test_filter_duplicate_edges():
    g = NodeGraph()
    nodes = [Node(-1, -1), Node(1, -1), Node(1, 1), Node(-1, 1)]
    for i, j in permutations(nodes, 2):
        g.add_line(i, j)

    assert len(g.edges) == 6


def test_coloring():
    g = NodeGraph(color="red")
    g.add_line_coords(0, 0, 1, 0)
    g.add_line_coords(1, 0, 1, 1)
    g.add_line_coords(1, 1, 0, 1)
    g.add_line_coords(0, 1, 0, 0)

    assert count_color(g) == 4

    assert g.color == "red"
    g.set_color_inner("green")
    assert g.color == "green"

    g.set_color_boundary("magenta")
    assert count_color(g, "magenta") == 4

    g.add_line_coords(1, 1, 5, 6, color="red")
    assert count_color(g, "red") == 1
    g.set_color_change("blue", "red")
    assert count_color(g, "red") == 0
    assert count_color(g, "blue") == 1
    assert count_color(g, "magenta") == 4


def test_rank():
    g = NodeGraph(rank=-1)
    assert g.rank == 1

    g.set_rank(111)
    assert g.rank == 111

    g.set_rank()
    assert g.rank == 0


def test_repr():
    g = NodeGraph()
    assert str(g) == "EMPTY GRAPH"
    g.add_line_coords(0, 0, 1, 0)
    print(g)  # a little cheating

    assert g.__repr__() == "G(v=2, e=1, c='none')"
