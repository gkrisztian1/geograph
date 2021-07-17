from nodegraph import Node
from nodegraph import NodeGraph
import matplotlib.pyplot as plt

def plot_graph(g: NodeGraph):
    plt.figure()

    for vi in g.vertices:
        plt.scatter(vi.x, vi.y, c='b')

    for ei in g.edges:
        plt.plot([ei.start.x, ei.end.x], [ei.start.y, ei.end.y], color=ei.color)

    plt.grid()
    plt.show()

g = NodeGraph(color='red')
g.add_line_coords(0, 0, 0, 1)
g.add_line_coords(0, 0, 1, 0)
g.add_line_coords(0, 0, 1, 1, color='green')
g.set_color_change('k', 'red')
plot_graph(g)
