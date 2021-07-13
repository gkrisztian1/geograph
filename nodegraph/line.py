from nodegraph import Node


class Line():
    def __init__(self, tail: Node, head: Node):
        self.start = tail
        self.end = head

    def set(self, *args, **kwargs):
        self.start.x = kwargs.get("x0", self.start.x)
        self.start.y = kwargs.get("y0", self.start.y)
        self.end.x = kwargs.get("x1", self.end.x)
        self.end.y = kwargs.get("y1", self.end.y)

    def __hash__(self):
        return self.start.id ^ self.end.id

    def __iter__(self):
        yield self.start.id
        yield self.end.id

    def __eq__(self, o):
        return hash(self) == hash(o)

    def __repr__(self):
        return f"L[{self.start} --> {self.end}]"
