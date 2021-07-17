from nodegraph import line
from nodegraph.line import Line
from nodegraph.node import Node
from nodegraph import Tree

"""
nodes should be hashable as well as edges,
but nodes should not be compared based on hash values !
"""


class NodeGraph:
    def __init__(self, color=0):
        self.color = color

        self.vertices = Tree()
        self.edges = set()

        # Bounding box that contains all the nodes and edges
        self.bbox_xmin = 0.0
        self.bbox_xmax = 0.0
        self.bbox_ymin = 0.0
        self.bbox_ymax = 0.0

    def add_node_coords(self, x, y):
        """This funciton adds a new Node instance to its vertex set based on the given coordinates.

        :x: The x coordinate of the Node
        :y: The y coordinate of the Node
        """
        self.add_node(Node(x, y))

    def add_node(self, n: Node):
        n = self.vertices.insert(n)

        if n.x < self.bbox_xmin:
            self.bbox_xmin = n.x

        if n.y < self.bbox_ymin:
            self.bbox_ymin = n.y

        if n.x > self.bbox_xmax:
            self.bbox_xmax = n.x

        if n.y > self.bbox_ymin:
            self.bbox_ymax = n.y

        return n

    def add_line_coords(self, xstart, ystart, xend, yend, color=None):
        """TODO: Docstring for add_line_coords.

        :xstart: TODO
        :ystart: TODO
        :xend: TODO
        :yend: TODO
        :color: TODO
        :returns: TODO

        """
        self.add_line(Node(xstart, ystart), Node(xend, yend), color=color)

    def add_line(self, start: Node, end: Node, color=None):
        if start != end:
            start = self.add_node(start)
            end = self.add_node(end)
            self.edges.add(Line(start, end, color=color))

    def set_color_boundary(self, color):
        """This function overwrites ALL of the lines' color."""
        for ei in self.edges:
            ei.set_color(color)

    def set_color_inner(self, color):
        """This fucntion changes the graphs color only, not the edges'."""
        self.color = color

    def set_color_change(self, original_color, new_color):
        """This function changes the colors of the edges that has original_color."""
        for ei in self.edges:
            if ei.color == original_color:
                ei.set_color(new_color)

    def __str__(self):
        if len(self.vertices) == 0:
            return "EMPTY GRAPH"

        st = "*" * 20
        st += f"\ncolor: {self.color}"
        st += f"\nBounding box: {self.bbox_xmin:.3f}, {self.bbox_ymin:.3f} - {self.bbox_xmax:.3f}, {self.bbox_ymax:.3f}\n"
        st += f"number of vertices: {len(self.vertices)}\n"
        st += f"number of edges: {len(self.edges)}\n"

        st += "\nVERTICES:\n"
        for vi in self.vertices:
            st += f"\t{vi}\n"

        st += "\nEDGES:\n"
        for ei in self.edges:
            st += f"\t{ei}\n"

        st += "\n" + "*" * 20

        return st

    def __repr__(self) -> str:
        return f"G('{self.color}')"
