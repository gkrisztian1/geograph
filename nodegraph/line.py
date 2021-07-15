from nodegraph import Node


class Line():
    def __new__(cls, tail: Node, head: Node):
        """
        If head and tail are structurally the same nodes then do not create an edge. (Prevent self loop).
        """
        if tail == head:
            return None
        else:
            return super(Line, cls).__new__(cls)

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
        return f"{self.start} --> {self.end}"



if __name__=='__main__':
    n1 = Node(4, 2)
    l1 = Line(n1, n1)
    print(l1)