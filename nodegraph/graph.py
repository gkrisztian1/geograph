# from nodegraph import getID
from nodegraph import Line
from nodegraph import Node
from nodegraph import binarySearchTree


class NodeGraph:

    def __init__(self):
        # self.id = getID()
        self.vertices = binarySearchTree()
        self.edges = set()

    def add_vertex(self, v: Node):
        return self.vertices.insert(v)

    def add_edge(self, tail: Node, head: Node):
        tail = self.add_vertex(tail)
        head = self.add_vertex(head)
        if (edge := Line(tail, head)):
            self.edges.add(edge)
            return True
        else:
            return False

    def __repr__(self) -> str:
        nodecounter = 0
        st = 'VERTICES:\n'
        for vi in self.vertices.depthFirstSearch_POSTorder():
            st += f'\t{vi}\n'
            nodecounter +=1

        st += f'\tnumber of vertices: {nodecounter}\n'
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
    # for i in range(N):
    #     g.add_edge(nodegenerator(), nodegenerator())


    # print(g)
    vertices = [nodegenerator() for i in range(N)]
    edges = {edge for _ in range(N) if (edge := Line(choice(vertices), choice(vertices))
                                        )}


    print(edges)
    print(len(edges))