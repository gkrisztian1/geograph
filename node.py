from numpy import arctan2, pi

class Node:
    tol = 1e-3

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.l2 = x**2 + y**2
        self.fi = arctan2(y, x) * 2 / pi

    def __bool__(self):
        return True

    def __eq__(self, o):
        if o is None:
            return False
        return (abs(self.x - o.x) < self.tol) and (abs(self.y - o.y) < self.tol)

    def __lt__(self, other):
        if not other:
            return False

        # return (self.l2 < other.l2) or (self.fi < other.fi)
        return self.fi <other.fi


    def __repr__(self):
        return f'(x={self.x}, y={self.y}, l2={self.l2}, fi={self.fi})'







