# from nodegraph import getID
from nodegraph import Line
from nodegraph import Node
from nodegraph import Tree


class NodeGraph:

    def __init__(self):
        # self.id = getID()
        self.vertices = Tree()
        self.edges = set()

        self.bbox = [0.0, 0.0, 0.0, 0.0]
        self.color = None

    def add_vertex(self, v: Node):
        v = self.vertices.insert(v)
        if v.x < self.bbox[0]:
            self.bbox[0] = v.x

        if v.y < self.bbox[1]:
            self.bbox[1] = v.y

        if v.x > self.bbox[2]:
            self.bbox[2] = v.x

        if v.y > self.bbox[3]:
            self.bbox[3] = v.y

        return v

    def add_edge(self, tail: Node, head: Node):
        tail = self.add_vertex(tail)
        head = self.add_vertex(head)

        if edge := Line(tail, head):
            self.edges.add(edge)

    def __repr__(self):
        nodecounter = 0
        st = 'VERTICES:\n'
        for vi in self.vertices:
            st += f'\t{vi}\n'
            nodecounter +=1

        st += f'\tnumber of vertices: {nodecounter}\n'
        st += f'\tbounding box: {self.bbox}\n'
        if self.color:
            st += f'\tcolor: {self.color}\n'
        edgecounter = 0
        st += "EDGES:\n"
        for ei in self.edges:
            st += f'\t{ei}\n'
            edgecounter += 1
        st += f'\tnumber of edges: {edgecounter}\n'
        return st


if __name__ == '__main__':
    from random import seed, randint, choice

    seed(42)
    N = 100
    xlim = (0, 1)
    ylim = (0, 1)
    nodegenerator = lambda : Node(randint(*xlim), randint(*ylim))

    g = NodeGraph()
    for i in range(N):
        g.add_edge(nodegenerator(), nodegenerator())


    print(g)
    print(g.bbox)
