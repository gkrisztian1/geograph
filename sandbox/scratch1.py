from nodegraph import Node
from nodegraph import NodeGraph


g = NodeGraph(color='red')
g.add_line_coords(0, 0, 0, 1)
g.add_line_coords(0, 0, 1, 0)
g.add_line_coords(0, 0, 1, 1, color='green')

print(g)
