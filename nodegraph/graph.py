from nodegraph import line
from nodegraph.line import Line
from nodegraph.node import Node
from nodegraph import Tree
from math import inf

"""
nodes should be hashable as well as edges,
but nodes should not be compared based on hash values !
"""


class NodeGraph:
    """
    This class implements a graph abstract data type which consist of vertices and edges. In this case the vertices are Node instances while edges
    are Line instances. A NodeGraph instance only have unique vertices and unique edges. All NodeGraph instance have a color and rank which
    helps grouping and identifying the said instance. A NodeGraph has a bounding box attribute that describes where the graph is located and
    how much space it covers.
    """

    def __init__(self, color="none", rank=None):
        """
        In the initialization phase we set the color and the rank values according to the arguments. (See later in this bit).
        We store the vertices in a Tree like data structure to ensure fast searching and insertion.

        :param color: holds the color of a graph but it can be used as a name, but generally color is used to group graph instances.
        :param rank: Rank is used when rendering the graph. The higher the number the prioritiy the graph has over other instances.
        """
        self.color = color
        self.set_rank(rank)

        self.vertices = Tree()
        self.edges = set()

        # Bounding box that contains all the nodes and edges
        self.bbox_xmin = inf
        self.bbox_xmax = -inf
        self.bbox_ymin = inf
        self.bbox_ymax = -inf

    def add_node_coords(self, x, y):
        """
        This function is used to conviniently add a node to a NodeGraph instance.
        """
        self.add_node(Node(x, y))

    def add_node(self, n: Node):
        """
        Use this function to insert a Node into the graph. DO NOT modify the vertices/edges attributes directly.
        If the node is present in the vertex tree then we return that Node object, otherwise we insert the new Node.

        After insertion we update the bounding box.
        """
        n = self.vertices.insert(n)

        if n.x < self.bbox_xmin:
            self.bbox_xmin = n.x

        if n.y < self.bbox_ymin:
            self.bbox_ymin = n.y

        if n.x > self.bbox_xmax:
            self.bbox_xmax = n.x

        if n.y > self.bbox_ymax:
            self.bbox_ymax = n.y

        return n

    def add_line_coords(
        self, xstart: float, ystart: float, xend: float, yend: float, color="none"
    ):
        """
        This function is used to quickly add an edge to the graph by its coordinates. You can spefify its color too.
        """
        self.add_line(Node(xstart, ystart), Node(xend, yend), color=color)

    def add_line(self, start: Node, end: Node, color="none"):
        """
        This function is used to add an edge to a graph instance. DO NO modify vertices/edges attributes directly.
        You can spefify the color of the edge too. This function prevents the creation of self-loops, which means you
        cannot add an edge that has the same starting point and ending point.
        """
        if start != end:
            start = self.add_node(start)
            end = self.add_node(end)
            self.edges.add(Line(start, end, name=color))

    def set_color_boundary(self, color):
        """This function overwrites ALL of the lines' color."""
        for ei in self.edges:
            ei.set_color(color)

    def set_color_inner(self, color):
        """This fucntion changes the graphs color only, not the edges'."""
        self.color = color

    def set_color_change(self, new_color, original_color="none"):
        """This function changes the colors of the edges that has original_color."""
        for ei in self.edges:
            if ei.color == original_color:
                ei.set_color(new_color)

    def set_rank(self, r=None):
        """This function sets the rank of the graph. Which can be any positive number. Higher numbers mean higher prioritiy."""
        self.rank = abs(int(0 if r is None else r))

    def __str__(self):
        """
        This function prints out the graphs properties as well as its nodes and edges.
        """
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
        """
        This function is for debugging purposes. It returns the number of vertices and edges that the graph holds as well
        as its color and rank.
        """
        return f"G(v={len(self.vertices)}, e={len(self.edges)}, c='{self.color}', r={self.rank})"
