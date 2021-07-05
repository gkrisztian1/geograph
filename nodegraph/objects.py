from abc import ABCMeta
from math import atan2, fmod, pi
from nodegraph import getID


class GeometryPiece(metaclass=ABCMeta):
    tol = 1e-3

    def __bool__(self):
        return True


class Node(GeometryPiece):
    def __init__(self, x, y):
        self.id = getID()
        self.x = float(x)
        self.y = float(y)
        self.l2 = self.x ** 2 + self.y ** 2
        self.fi = atan2(self.y, self.x) * 180.0 / pi

        if self.fi < -self.tol:
            self.fi += 360.0

        self.fi = fmod(self.fi + self.tol, 360.0) - self.tol

    def __eq__(self, o):
        return (abs(self.x - o.x) < self.tol) and (abs(self.y - o.y) < self.tol)

    def __lt__(self, o):
        diff = self.l2 - o.l2

        if abs(diff) < self.tol:
            if (self.fi - o.fi) < -self.tol:
                return True
            else:
                return False
        elif diff < -self.tol:
            return True
        else:
            return False

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.l2}, {self.fi})"


class Line(GeometryPiece):
    def __init__(self, tail: Node, head: Node):
        self.start = tail
        self.end = head

    def __iter__(self):
        yield self.start.id
        yield self.end.id

    def __eq__(self, o):
        return len(set(self) | set(o)) == 2

    def __repr__(self):
        return f"{self.tail} --> {self.head}"
