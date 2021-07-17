from nodegraph.node import Node


class Line:
    def __new__(cls, tail: Node, head: Node, **kwargs):
        """
        If head and tail are structurally the same nodes then do not create an edge. (Prevent self loop).
        """
        if tail == head:
            return None
        else:
            return super(Line, cls).__new__(cls)

    def __init__(self, start: Node, end: Node, color=None):
        self.start = start
        self.end = end

        self.color = color or "k"
        self.weight = self._calc_weight()

    def set_color(self, color):
        self.color = color

    def _calc_weight(self):
        """This function calculates the weight of a line between 2 nodes."""
        return abs(self.end - self.start)

    def __hash__(self):
        return self.start.id ^ self.end.id

    def __bool__(self):
        """this will be 0 if tail == head"""
        return bool(hash(self))

    def __iter__(self):
        yield self.start
        yield self.end

    def __eq__(self, o):
        return hash(self) == hash(o)

    def __repr__(self):
        st = f"{self.start} - {self.end} w: {self.weight:.3f}"
        return st + f" c: {self.color}" if self.color != "k" else st
