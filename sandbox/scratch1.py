from nodegraph import Geometry
from nodegraph import NodeGraph
from nodegraph import paths
import matplotlib.pyplot as plt

def plot_graph(g: NodeGraph):
    plt.figure()

    for vi in g.vertices:
        plt.scatter(vi.x, vi.y, c='b')

    for ei in g.edges:
        plt.plot([ei.start.x, ei.end.x], [ei.start.y, ei.end.y], color=ei.color)

    plt.grid()
    plt.show()


geom = Geometry()
geom.import_svg(paths.path_resources / '3poly.svg' )

print(geom.graphs)
geom.plot_geometry()
