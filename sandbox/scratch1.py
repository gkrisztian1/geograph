from os import stat
from nodegraph import Geometry
from nodegraph import NodeGraph
from nodegraph import paths
import matplotlib.pyplot as plt


blue = NodeGraph(color="blue", rank=10)
blue.add_line_coords(0, 0, 10, 0)
blue.add_line_coords(10, 0, 10, 10)
blue.add_line_coords(10, 10, 0, 10)
blue.add_line_coords(0, 10, 0, 0)

green = NodeGraph(color="green", rank=0)
green.add_line_coords(6, 3, 14, 3)
green.add_line_coords(14, 3, 14, 7)
green.add_line_coords(14, 7, 6, 7)
green.add_line_coords(6, 7, 6, 3)

geom = Geometry()
geom.graphs.append(blue)
geom.graphs.append(green)


geom.plot_geometry(bbox=False, show=True)
print(geom)

geom._generate_intersection_queue()
