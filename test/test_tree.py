from nodegraph import binarySearchTree
from nodegraph import Node
from random import randint, uniform

def test_filter_node_duplicates():
    noise = lambda : uniform(-1e-5, 1e-5)
    tree = binarySearchTree()

    for i in range(500):
        X = randint(-1, 1) + noise()
        Y = randint(-1, 1) + noise()
        tree.insert(Node(X, Y))

    assert len(list(tree.depthFirstSearch_POSTorder())) == 9