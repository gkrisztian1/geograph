from nodegraph import Geometry
from nodegraph import NodeGraph
from nodegraph import paths
import matplotlib.pyplot as plt

geom = Geometry()
geom.import_svg(paths.path_resources / '3poly.svg' , verbose=True)

# geom.plot_geometry(bbox=True)
print(geom)

geom._generate_intersection_queue()
