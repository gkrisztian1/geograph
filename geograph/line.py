from geograph import getID
from geograph.node import Node
from itertools import chain
from collections.abc import Hashable

class Line:
    def __new__(cls, tail: Node, head: Node, **kwargs):
        """
        If head and tail are structurally the same nodes then do not create an edge. (Prevent self loop).
        """
        if tail == head:
            return None
        else:
            return super(Line, cls).__new__(cls)

    def __init__(self, start: Node, end: Node, name:Hashable=None, group:Hashable=None, **kwargs):
        self.start = start
        self.end = end
        self.name = name
        self.group = group
        self.bbox = None
        self.center_point = None


        self.weight = self._calc_weight()
        self._update_bbox()

    def _calc_weight(self):
        """This function calculates the weight of a line between 2 nodes."""
        return abs(self.end - self.start)

    def _update_bbox(self):
        xmin, xmax = sorted([self.start.x, self.end.x])
        ymin, ymax = sorted([self.start.y, self.end.y])

        self.bbox = (Node(xmin, ymin), Node(xmax, ymax))
        self.center_point = self.bbox[0] + 0.5 * (self.bbox[1] - self.bbox[0])


    def __hash__(self):
        return hash(self.start) ^ hash(self.end)

    def __bool__(self):
        return self.weight < 1e-5

    def __iter__(self):
        yield from chain(self.start, self.end)

    def __eq__(self, o):
        return hash(self) == hash(o)

    def __repr__(self):
        st = f"{self.start} - {self.end} w: {self.weight:.3f}"
        return st + f" c: {self.name}" if self.name is not None else st
