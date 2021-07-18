from nodegraph import Geometry, Node, NodeGraph
from nodegraph import paths


def test_creation():
    geom = Geometry()
    assert geom.rank == 0

    # cheating the unnecessary parts
    g = NodeGraph()
    g.add_line_coords(0, 0, 1, 0, color="red")
    geom.graphs.append(g)
    print(geom)
    geom.plot_geometry(bbox=True)


def test_svg_read():
    g = Geometry()
    g.import_svg(paths.path_resources / "test1.svg")

    assert g.nb_nodes == 32
    assert g.nb_edges == 32
