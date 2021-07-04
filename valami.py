from random import shuffle
from nodegraph import Node
import operator

a = Node(1, 1)
b = Node(0, 1)
c = Node(-1, 1)
d = Node(1, 0)
e = Node(0, 0)
f = Node(-1, 0)
g = Node(1, -1)
h = Node(0, -1)
i = Node(-1, -1)

nodes  = [a, b, c, d, e, f, g, h, i]
shuffle(nodes)
nodes.sort()

reference_nodes = [e, d, b, f, h, a, c, i, g]
print(list(map(operator.eq, nodes, reference_nodes)))


from nodegraph import Line

l1 = Line(a, b)
l2 = Line(b, a)
print(l1==l2)
