import numpy as np
from node import Node
from tree import binarySearchTree
from random import seed, randint, uniform




seed(99)
noise = lambda : uniform(-1e-5, 1e-5)

N = 500
bst = binarySearchTree()
bases = set()
for i in range(N):
    X = randint(-1,1)
    Y = randint(-1, 1)
    bases.add((X, Y))


    node = Node(X, Y)

    X += noise()
    Y += noise()
    bst.insert(node)



print('POST order:')
a = bst.depthFirstSearch_POSTorder()
for ai in a:
    print(ai)

print(len(a))
print(bases)


