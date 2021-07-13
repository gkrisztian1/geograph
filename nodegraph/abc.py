from abc import ABCMeta, abstractmethod
from nodegraph import getID

class Vertex(metaclass=ABCMeta):
    def __init__(self):
        self.id = getID()

    def __hash__(self):
        return self.id

    @abstractmethod
    def __bool__(self):
        ...

    @abstractmethod
    def __eq__(self, o):
        ...

    @abstractmethod
    def __lt__(self, other):
        ...


class Edge:
    def __init__(self, tail: Vertex, head: Vertex, color=None):
        self.head = head
        self.tail = tail
        self.weight = None
        self.color = color or None

    def __hash__(self):
        return self.head.id ^ self.tail.id

    def __iter__(self):
        yield self.start.id
        yield self.end.id

    def __eq__(self, o):
        return hash(self) == hash(o)

    def __repr__(self):
        return f"L[{self.start} --> {self.end}]"