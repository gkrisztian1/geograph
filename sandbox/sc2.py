from geograph import Node
from geograph import Line
import itertools


nodes = [Node(0, 0), Node(0, 1), Node(1, 0), Node(1, 1)]
A = set()
for comb_i in itertools.permutations(nodes, r=2):
    l = Line(*comb_i)
    print(bool(l), l, hash(l))
    A.add(l)

print("-"*12)
print(A)
print(len(A))
