from os import stat
from nodegraph import Geometry
from nodegraph import NodeGraph
from nodegraph import paths
import matplotlib.pyplot as plt
import cProfile
import pstats

with cProfile.Profile() as pr:
    geom = Geometry()
    geom.import_svg(paths.path_resources / "3poly.svg", verbose=True)

    # geom.plot_geometry(bbox=True)
    print(geom)

    geom._generate_intersection_queue()

stats = pstats.Stats(pr)
stats.sort_stats(pstats.SortKey.TIME)
stats.dump_stats(filename="needed_profiling.prof")
