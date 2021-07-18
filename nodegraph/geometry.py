from collections import deque
import svgpathtools as svg
from nodegraph import NodeGraph
import matplotlib.pyplot as plt
from nodegraph import hex2name


class Geometry:
    def __init__(self, rank=0):
        self.graphs = list()
        self.rank = int(rank)

        self.intersection_queue = deque()

        self.nb_nodes = 0
        self.nb_edges = 0
        self.colorset_inner = set()
        self.colorset_boundary = set()

    def _bbox_intersect(self, g1: NodeGraph, g2: NodeGraph):
        g1_left = g1.bbox_xmin
        g1_right = g1.bbox_xmax
        g1_top = g1.bbox_ymax
        g1_bottom = g1.bbox_ymin

        g2_left = g2.bbox_xmin
        g2_right = g2.bbox_xmax
        g2_top = g2.bbox_ymax
        g2_bottom = g2.bbox_ymin

        return not (
            (g2_left > g1_right)
            or (g2_right < g1_left)
            or (g2_top < g1_bottom)
            or (g2_bottom > g1_top)
        )

    def _generate_intersection_queue(self):
        for i in range(len(self.graphs)):
            for j in range(i + 1, len(self.graphs)):
                if self._bbox_intersect(self.graphs[i], self.graphs[j]):
                    self.intersection_queue.append((i, j))

        while self.intersection_queue:
            print(self.intersection_queue.pop())

    def import_svg(self, file_name, verbose=False):
        paths, attribures, svg_attributes = svg.svg2paths2(str(file_name))

        # if verbose:
        #     for key, value in svg_attributes.items():
        #         print(key, value)
        #     print('-'*20)

        for attr_i, path_i in zip(attribures, paths):
            attr_i = [attr_ij.split(":") for attr_ij in attr_i.get("style").split(";")]
            attr_i = {stlye_key: style_value for stlye_key, style_value in attr_i}
            color_graph = attr_i.get("fill", "none")
            color_paths = attr_i.get("stroke", "none")
            c1 = hex2name(color_graph)
            c2 = hex2name(color_paths)
            self.colorset_inner.add(c1)
            self.colorset_boundary.add(c2)

            if verbose:
                # print(f"inner color: {color_graph}, boundary color: {color_paths}")
                print(f"from {color_graph}, {color_paths} to {c1}, {c2}")

            g = NodeGraph(color=c1)
            for pi in path_i:
                tail = -pi.start
                head = -pi.end

                g.add_line_coords(
                    -tail.real, tail.imag, -head.real, head.imag, color=c2
                )

            self.graphs.append(g)
            self.nb_nodes += len(g.vertices)
            self.nb_edges += len(g.edges)

        if verbose:
            print("-" * 20)

    def plot_geometry(self, bbox=False):
        fig, ax = plt.subplots()

        for gi in self.graphs:

            x = []
            y = []
            for ei in gi.edges:
                x.append(ei.start.x)
                x.append(ei.end.x)
                y.append(ei.start.y)
                y.append(ei.end.y)
                ax.plot([ei.start.x, ei.end.x], [ei.start.y, ei.end.y], color=ei.color)

            ax.fill(x, y, gi.color, alpha=1.0)

            for vi in gi.vertices:
                ax.scatter(vi.x, vi.y, c="r")

            if bbox:
                ax.plot(
                    [gi.bbox_xmin, gi.bbox_xmax],
                    [gi.bbox_ymin, gi.bbox_ymin],
                    "k-",
                    linewidth=0.5,
                )
                ax.plot(
                    [gi.bbox_xmin, gi.bbox_xmax],
                    [gi.bbox_ymax, gi.bbox_ymax],
                    "k-",
                    linewidth=0.5,
                )

                ax.plot(
                    [gi.bbox_xmin, gi.bbox_xmin],
                    [gi.bbox_ymin, gi.bbox_ymax],
                    "k-",
                    linewidth=0.5,
                )
                ax.plot(
                    [gi.bbox_xmax, gi.bbox_xmax],
                    [gi.bbox_ymin, gi.bbox_ymax],
                    "k-",
                    linewidth=0.5,
                )

        # plt.grid()
        plt.show()

    def __str__(self):
        st = "-" * 20 + "\n"
        st += f"number of graphs: {len(self.graphs)}\n"
        st += f"number of nodes:  {self.nb_nodes}\n"
        st += f"number of edges:  {self.nb_edges}\n"
        st += "inner colors: " + ", ".join(self.colorset_inner) + "\n"
        st += "boundary colors: " + ", ".join(self.colorset_boundary) + "\n"

        st += "-" * 20 + "\n"
        return st
