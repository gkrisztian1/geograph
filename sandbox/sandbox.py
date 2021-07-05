from nodegraph import Node
from nodegraph import Line


n1 = Node(4,5)
n2 = Node(54,-4.3443)

l1 = Line(n1, n2)
l2 = Line(n2, n1)

print(l1==l2)
print(l1)