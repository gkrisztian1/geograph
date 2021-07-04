from nodegraph import Node

def test_node_eq():

    n1 = Node(1, 0)
    n2 = Node(1, 0)
    assert n1==n2
