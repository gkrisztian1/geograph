from collections import defaultdict
import svgpathtools as svg
from nodegraph import NodeGraph
import matplotlib.pyplot as plt

class Geometry():
    def __init__(self, rank=0):
        self.graphs  = defaultdict(list)
        self.rank = int(rank)

    def import_svg(self, file_name):
        paths, attribures, svg_attributes = svg.svg2paths2(str(file_name))

        # for key, value in svg_attributes.items():
        #     print(key, value)

        # print('-'*20)
        for attr_i, path_i in zip(attribures, paths):
            attr_i = [attr_ij.split(':') for attr_ij in attr_i.get('style').split(';')]
            attr_i = {stlye_key: style_value for stlye_key, style_value in attr_i}
            color_graph = attr_i.get('fill', 'k')
            color_paths = attr_i.get('stroke', 'k')

            if color_graph == 'none':
                color_graph = 'k'

            if color_paths == 'none':
                color_paths = 'k'

            g = NodeGraph(color=color_graph)
            for pi in path_i:
                xstart = pi.start.real
                ystart = -pi.start.imag
                xend = pi.end.real
                yend = -pi.end.imag
                g.add_line_coords(xstart, ystart, xend, yend, color=color_paths)

            self.graphs[color_graph].append(g)


    def plot_geometry(self):
        fig, ax = plt.subplots()

        for color_i, graphlist in self.graphs.items():
            for gi in graphlist:
                for ei in gi.edges:
                    ax.plot([ei.start.x, ei.end.x], [ei.start.y, ei.end.y], color=ei.color)

                for vi in gi.vertices:
                    ax.scatter(vi.x, vi.y, c='b')

        plt.grid()
        plt.show()


