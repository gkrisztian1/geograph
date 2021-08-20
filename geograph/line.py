import math
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

    def __init__(
        self,
        start: Node,
        end: Node,
        name: Hashable = None,
        group: Hashable = None,
        **kwargs,
    ):
        self.start = start
        self.end = end
        self.unitvector = self.start.unitvector(self.end)
        self.length = 0.0

        self.name = name
        self.group = group

        self.bbox = None
        self.center_point = None

        self._update()

    def set_length(self, new_length: float, ref_pt="center"):
        """
        This function sets the length of the line inplace. The line can be streched in different ways based on the ref_pt argument.
        The default behavior is to strech/shrink each end of the line with new_length/2. Accepted ref_pt values are:

        - "center": both the start and endpoint will move along the line with new_length/2
        - "start": start point stays and the endpoint will move new_length
        - "end": endpoint stays and the startpoint will move new_length

        """
        assert new_length > 0.0

        if ref_pt == "center":
            self.start = self.center_point - self.unitvector * new_length / 2
            self.end = self.center_point + self.unitvector * new_length / 2

        elif ref_pt == "start":
            self.end = self.start + self.unitvector * new_length

        elif ref_pt == "end":
            self.start = self.end - self.unitvector * new_length
        else:
            raise ValueError(
                f"Invalid value for ref_pt. Accepted values are 'center', 'start', 'end'.Got {ref_pt=}."
            )

        self._update()

    def translate(self, dx, dy):
        """
        This funciton translates both the startpoint and enpoint to dx and dy.
        """
        self.start += (dx, dy)
        self.end += (dx, dy)
        self._update()

    def move(self, xn, yn, ref_pt="center"):
        """
        This funciton moves the line to a new location. The selected ref_pt will touch the (xn, yn) point.
        Accepted values for ref_pt: 'center', 'start', 'end'
        """
        fx_pt = Node(xn, yn)
        delta = None
        if ref_pt == "center":
            delta = fx_pt - self.center_point

        elif ref_pt == "start":
            delta = fx_pt - self.start

        elif ref_pt == "end":
            delta = fx_pt - self.end

        else:
            raise ValueError(
                f"Invalid value for ref_pt. Accepted values are 'center', 'start', 'end'.Got {ref_pt=}."
            )

        self.translate(delta.x, delta.y)

    def rotate(self, alpha, fx_pt=(0.0, 0.0), ref_pt=None):
        """ """

        if ref_pt == "start":
            fx_pt = Node(*self.start)
        elif ref_pt == "center":
            fx_pt = Node(*self.center_point)
        elif ref_pt == "end":
            fx_pt = Node(*self.end)
        elif ref_pt is None:
            fx_pt = Node(0, 0)
        else:
            raise ValueError(
                f"Invalid value for ref_pt. Accepted values are 'center', 'start', 'end'.Got {ref_pt=}."
            )

        self.start.rotate(alpha, ref_pt=fx_pt)
        self.end.rotate(alpha, ref_pt=fx_pt)
        self._update()

    def _update(self):
        self._update_length()
        self._update_bbox()

    def _update_length(self):
        """This function calculates the length of the line between 2 nodes."""
        self.length = abs(self.end - self.start)

    def _update_bbox(self):
        xmin, xmax = sorted([self.start.x, self.end.x])
        ymin, ymax = sorted([self.start.y, self.end.y])

        self.bbox = (Node(xmin, ymin), Node(xmax, ymax))
        self.center_point = self.bbox[0] + 0.5 * (self.bbox[1] - self.bbox[0])

    def __hash__(self):
        return hash(self.start) ^ hash(self.end)

    def __bool__(self):
        return self.length > 1e-5

    def __iter__(self):
        yield from chain(self.start, self.end)

    def __eq__(self, o):
        return hash(self) == hash(o)

    def __repr__(self):
        st = f"{self.start} - {self.end} w: {self.length:.3f}"
        return st + f" c: {self.name}" if self.name is not None else st
