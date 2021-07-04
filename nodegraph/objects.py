from abc import ABCMeta
from math import atan2, fmod, pi
from nodegraph import getID


class GeometryPiece(metaclass=ABCMeta):
    tol=1e-3

class Node(GeometryPiece):

    def __init__(self, x, y):
        self.id = getID()
        self.x = float(x)
        self.y = float(y)
        self.l2 = self.x**2 + self.y**2
        self.fi = atan2(self.y, self.x) * 180.0 / pi

        if self.fi < 0:
            self.fi += 360

        self.fi = fmod(self.fi, 360.0-self.tol)

    def __bool__(self):
        return self.l2 > self.tol**2 

    def __eq__(self, o):
        if o:
            return (abs(self.x - o.x) < self.tol) and (abs(self.y - o.y) < self.tol)
        else:
            return False

    def __lt__(self, o):
        if not o:
            return False

        if (self.l2 - o.l2) < -self.tol:
            return True
        elif (self.fi - o.fi) < -self.tol:
            return True
        else: False

    def __repr__(self):
        return f'(x={self.x}, y={self.y}, l2={self.l2}, fi={self.fi})'



def Line(GeometryPiece):

    def __init__(self, head: Node, tail: Node):
        self.start = tail
        self.end = head  

    def __iter__(self):
        yield self.start.id
        yield self.end.id

    def __eq__(self, o):
        return not (set(self) - set(o))















