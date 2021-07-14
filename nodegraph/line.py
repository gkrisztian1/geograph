from nodegraph import Node


class Line():
    def __init__(self, tail: Node, head: Node):
        self.start = tail
        self.end = head

    def __hash__(self):
        return self.start.id ^ self.end.id

    def __bool__(self):
        """ this will be 0 if tail == head """
        return bool(hash(self))

    def __iter__(self):
        yield self.start.id
        yield self.end.id

    def __eq__(self, o):
        return hash(self) == hash(o)

    def __repr__(self):
        return f"L[{self.start} --> {self.end}]"
