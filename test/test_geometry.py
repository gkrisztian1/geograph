from nodegraph import Geometry, Node, NodeGraph


def test_creation():
    geom = Geometry()
    assert geom.rank == 0

    # cheating the unnecessary parts
    g = NodeGraph()
    g.add_line_coords(0, 0, 1, 0, color="red")
    geom.graphs.append(g)
    print(geom)
    geom.plot_geometry(bbox=True)
