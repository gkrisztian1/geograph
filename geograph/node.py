from typing import Iterable
from numbers import Real
from math import atan2, fmod, pi, sqrt
from geograph import getID
import operator
import itertools


class Node:
    tol = 1e-3
    __slots__ = ("name", "group", "vec", "l2", "phi")

    def __init__(self, x, y, name=None, group=None):
        self.name = name or getID()
        self.group = group
        self.vec = (float(x), float(y))

        self._update_l2()
        self._update_phi()

    def set(self, **kwargs):
        x = kwargs.get("x", self.vec[0])
        y = kwargs.get("y", self.vec[1])
        self.vec = (x, y)

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

        return self.phi

    def _do_operator(self, value, operator_):
        """
        This is a general method to execute varius modification on a Node instance.

        :param value: Any Iterable or Real object is acceptable
        :param operator_: this is a function that executes the operator in an operator_(own_coordinate_i, value_i) way.
        :return: The return value is a generator expression containing the results of the operator_s effect
         on the coordinates.
        """
        # If value is a single number then we create a repeater object to be able to "iterate" over it.
        if isinstance(value, Real):
            value = itertools.repeat(value)

        return map(operator_, self, value)

    def __getattr__(self, item):
        """
        Still supporting node.x and node.y to quickly access the coordinates
        :param item: can be 'x' or 'y'
        :return:
        """
        if item == "x":
            return self.vec[0]
        elif item == "y":
            return self.vec[1]
        else:
            raise AttributeError(f"Node does not have {item} attribute")

    def __eq__(self, o):
        """
        If the absolute difference between each coordinate is less than the tolerance then the
        2 Nodes are equal.

        :param o: It can be any iterable object, but another Node instance is preferred
        :return: True or False
        """
        if isinstance(o, Iterable):
            return all(
                self._do_operator(o, lambda own, other: abs(own - other) < self.tol)
            )
        else:
            return False

    def __lt__(self, o):
        """
        This function compares the operands l2 value with its l2 value. If they're equal (whitin tolerance)
        that means the nodes are on the same circle. If that's the case then check their angle and return accordingly.
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
        """Support array indexing for ease of use."""
        return self.vec[key]

    def __iter__(self):
        """This function YEETs out the coordinates one by one."""
        yield from self.vec

    def __add__(self, val):
        """Create a new Node instance with the val addition"""
        return Node(*self._do_operator(val, operator.add))

    def __radd__(self, val):
        """This falls back to the other addition"""
        return self + val

    def __iadd__(self, val):
        """
        This function is doing an addition inplace. Use the general _do_operator function and consumne the returned
        generator expression to create a new tuple object to hold the modified coordinates.
        """
        self.vec = tuple(self._do_operator(val, operator.add))
        return self

    def __sub__(self, val):
        """Create a new Node instance with the val subtraction"""
        return Node(*self._do_operator(val, operator.sub))

    def __rsub__(self, val):
        """You can't do this if val is a number. Iterable case is fine."""
        if isinstance(val, Real):
            raise ValueError("You cannot subtract a Node from a number.")
        else:
            return Node(*map(operator.sub, val, self))

    def __isub__(self, val):
        """
        This function is doing a subtraction inplace. Use the general _do_operator function and consumne the returned
        generator expression to create a new tuple object to hold the modified coordinates.
        """
        self.vec = tuple(self._do_operator(val, operator.sub))
        return self

    def __mul__(self, val):
        """
        Multiplication with an Iterable object will result the dot product between self and val. Otherwise scale the
        coordinates according to val.
        """
        if isinstance(val, Iterable):
            return sum(self._do_operator(val, operator.mul))
        else:
            return Node(*self._do_operator(val, operator.mul))

    def __rmul__(self, val):
        return self * val

    def __imul__(self, val):
        if not isinstance(val, Iterable):
            self.vec = tuple(self._do_operator(val, operator.mul))
        else:
            raise ValueError(
                "You cannot do this. Use dot product or cross product instead."
            )

    def __matmul__(self, other):
        """
        This function returns the cross product between 2 Node instances. ue 'a @ b' for shortcut.
        """
        # v1x * v2y - v1y * v2x
        return self.x * other.y - self.y * other.x

    def __abs__(self):
        return sqrt(self.l2)

    def __copy__(self):
        return Node(*self)

    def __repr__(self):
        return f"N({self[0]}, {self[1]})"
        # return f"({self[0]}, {self[1]}, {self.l2}, {self.fi})"

    def __hash__(self):
        return id(self)
