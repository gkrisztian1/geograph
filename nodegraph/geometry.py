from collections import deque
from collections.abc import Iterable
import svgpathtools as svg
from nodegraph import NodeGraph
import matplotlib.pyplot as plt
from nodegraph import hex2name
import numpy as np


class Geometry:
    def __init__(self, rank=0):
        self.graphs = list()
        self.rank = int(rank)

        self.intersection_queue = deque()

        self.nb_nodes = 0
        self.nb_edges = 0
        self.colorset_inner = set()
        self.colorset_boundary = set()

    def _generate_intersection_queue(self):
        for i in range(len(self.graphs)):
            for j in range(i + 1, len(self.graphs)):
                r1 = (
                    self.graphs[i].bbox_xmin,
                    self.graphs[i].bbox_ymin,
                    self.graphs[i].bbox_xmax,
                    self.graphs[i].bbox_ymax,
                )

                r2 = (
                    self.graphs[j].bbox_xmin,
                    self.graphs[j].bbox_ymin,
                    self.graphs[j].bbox_xmax,
                    self.graphs[j].bbox_ymax,
                )

                if self.is_rectangle_intersect(r1, r2):
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
            self._generate_intersection_queue()

        if verbose:
            print("-" * 20)

    def plot_geometry(self, bbox=False, show=False):
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
        if show:
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

    @staticmethod
    def is_rectangle_intersect(r1: Iterable, r2: Iterable):

        r1_left, r1_bottom, r1_right, r1_top = r1
        r2_left, r2_bottom, r2_right, r2_top = r2

        assert r1_left <= r1_right, f"Not a proper bounding box: {r1}"
        assert r2_left <= r2_right, f"Not a proper bounding box: {r2}"
        assert r1_bottom <= r1_top, f"Not a proper bounding box: {r1}"
        assert r2_bottom <= r2_top, f"Not a proper bounding box: {r2}"

        return not (
            (r2_left > r1_right)
            or (r2_right < r1_left)
            or (r2_top < r1_bottom)
            or (r2_bottom > r1_top)
        )

    @staticmethod
    def get_intersections(p1x, p1y, q1x, q1y, p2x, p2y, q2x, q2y, epsilon=1e-3):
        """
        :param line_1: the first line
        :param line_2: second line
        :returns: () or ((x, y)) or ((x1, y1), (x2, y2))
        https://stackoverflow.com/questions/563198/how-do-you-detect-where-two-line-segments-intersect
        Conditions:
        1. If r × s = 0 and (q − p) × r = 0, then the two lines are collinear.
        2. If r × s = 0 and (q − p) × r ≠ 0, then the two lines are parallel and non-intersecting.
        3. If r × s ≠ 0 and 0 ≤ t ≤ 1 and 0 ≤ u ≤ 1, the two line segments meet at the point p + t r = q + u s.
        4. Otherwise, the two line segments are not parallel but do not intersect.
        """

        intersection_points = list()
        p1 = None
        p2 = None

        p = np.array([p1x, p1y])
        r = np.array([q1x - p1x, q1y - p1y])

        q = np.array([p2x, p2y])
        s = np.array([q2x - p2x, q2y - p2y])

        test1 = np.abs(np.cross(r, s))
        test2 = np.abs(np.cross((q - p), r))

        t0 = np.dot(q - p, r) / np.dot(r, r)
        t1 = t0 + np.dot(s, r) / np.dot(r, r)
        t2 = np.dot(p - q, s) / np.dot(s, s)
        t3 = t2 + np.dot(r, s) / np.dot(s, s)

        inrange = lambda x: x > (0 - epsilon) and x < (1 + epsilon)
        distance = lambda x, y: np.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)

        if test1 < epsilon:

            if test2 < epsilon:

                if inrange(t0):
                    p1 = tuple(p + t0 * r)

                if inrange(t1):
                    p2 = tuple(p + t1 * r)

                if inrange(t2):
                    p1 = tuple(q + t2 * s)

                if inrange(t3):
                    p2 = tuple(q + t3 * s)

        else:
            up = (
                -p1x * q1y + p1x * p2y + q1x * p1y - q1x * p2y - p2x * p1y + p2x * q1y
            ) / (
                p1x * p2y
                - p1x * q2y
                - q1x * p2y
                + q1x * q2y
                - p2x * p1y
                + p2x * q1y
                + q2x * p1y
                - q2x * q1y
            )
            tp = (
                p1x * p2y - p1x * q2y - p2x * p1y + p2x * q2y + q2x * p1y - q2x * p2y
            ) / (
                p1x * p2y
                - p1x * q2y
                - q1x * p2y
                + q1x * q2y
                - p2x * p1y
                + p2x * q1y
                + q2x * p1y
                - q2x * q1y
            )
            if inrange(tp) and inrange(up):
                p1 = tuple(p + tp * r)

        if (p1 is not None) and (p2 is not None) and (distance(p1, p2) < epsilon):
            p2 = None

        if p1 is not None:
            intersection_points.append(p1)

        if p2 is not None:
            intersection_points.append(p2)

        return intersection_points
