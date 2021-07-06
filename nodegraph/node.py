from typing import Iterable
from numbers import Real
from nodegraph.abc import GeometryPiece
from math import atan2, fmod, pi
from nodegraph import getID
import operator


class Node(GeometryPiece):
    def __init__(self, x, y):
        self.id = getID()
        self.x = float(x)
        self.y = float(y)

        self._update_l2()
        self._update_phi()

    def set(self, *args, **kwargs):
        self.x = kwargs.get('x', self.x)
        self.y = kwargs.get('y', self.y)

    def _update_l2(self):
        """
        This function calculates the squared distance of a point from the origin.
        """
        self.l2 = self.x ** 2 + self.y ** 2

    def _update_phi(self):
        """
        This function calculates the angle between the node and the x axis.
        :return [0, 360]
        """
        self.phi = atan2(self.y, self.x) * 180.0 / pi

        if self.phi < -self.tol:
            self.phi += 360.0

        self.phi = fmod(self.phi + self.tol, 360.0) - self.tol

    def __eq__(self, o):
        """
        If the absolute difference between each coordinate is less than the tolerance then the
        2 Nodes are equal.

        :param o: Should be other Node instance otherwise it throws an exception
        :return: True or False
        """
        return (abs(self.x - o.x) < self.tol) and (abs(self.y - o.y) < self.tol)

    def __lt__(self, o):
        """
        This function compares the operands l2 value with its l2 value. If they're equal (whitin tolerance)
        that means the nodes are on the same circle. If that's the case then check their angle return accordingly.
        If the l2 values are different then one node is obviously bigger than the other. In that case check the
        differences sign.
        :param o: other Node
        :return: True or False
        """
        diff = self.l2 - o.l2

        if abs(diff) < self.tol:
            # They're on the same circle, more checks needed to decide
            if (self.phi - o.phi) < -self.tol:
                return True
            else:
                return False
        elif diff < -self.tol:
            return True
        else:
            return False

    def __getitem__(self, key):
        ...

    def __iter__(self):
        yield self.x
        yield self.y

    def __add__(self, val):
        if isinstance(val, Iterable):
            return Node(*map(operator.add, self, val))
        elif isinstance(val, Real):
            return Node(self.x + val, self.y + val)
        else:
            raise NotImplementedError()

    def __radd__(self, val):
        return self + val

    def __iadd__(self, val):
        ...

    def __sub__(self, val):
        ...

    def __rsub__(self, val):
        return self - val

    def __isub__(self, val):
        ...

    def __mul__(self, val):
        ...

    def __rmul__(self, val):
        ...

    def __imul__(self, val):
        ...

    def __copy__(self):
        return Node(self.x, self.y)

    def __repr__(self):
        return f"N({self.x:.3f}, {self.y:.3f})"
        # return f"({self.x}, {self.y}, {self.l2}, {self.fi})"


