from nodegraph import getID
from nodegraph.node import Node
from itertools import chain


class Line:
    def __new__(cls, tail: Node, head: Node, **kwargs):
        """
        If head and tail are structurally the same nodes then do not create an edge. (Prevent self loop).
        """
        if tail == head:
            return None
        else:
            return super(Line, cls).__new__(cls)

    def __init__(self,start: Node, end: Node, name=None, group=None, **kwargs):
        self.start = start
        self.end = end

        self.name = name or getID()
        self.group = group
        self.weight = self._calc_weight()

    def set_color(self, color):
        self.color = color

    def get_bbox(self):
        xmin = self.start.x if self.start.x < self.end.x else self.end.x
        xmax = self.start.x if self.start.x > self.end.x else self.end.x
        ymin = self.start.y if self.start.y < self.end.y else self.end.y
        ymax = self.start.y if self.start.y > self.end.y else self.end.y

        return (xmin, ymin, xmax, ymax)

    def _calc_weight(self):
        """This function calculates the weight of a line between 2 nodes."""
        return abs(self.end - self.start)

    def __hash__(self):
        return self.start.name ^ self.end.name

    def __bool__(self):
        """this will be 0 if tail == head"""
        return bool(hash(self))

    def __iter__(self):
        yield from chain(self.start, self.end)

    def __eq__(self, o):
        return hash(self) == hash(o)

    def __repr__(self):
        st = f"{self.start} - {self.end} w: {self.weight:.3f}"
        return st + f" c: {self.color}" if self.color != "k" else st
