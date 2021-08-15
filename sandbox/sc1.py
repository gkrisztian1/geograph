from copy import copy
from geograph import Node, Line
import math
import matplotlib.pyplot as plt

plt.style.use(['default', 'fast'])

def render_line(ax, l:Line):
    
    x0, y0, x1, y1 = l
    ax.plot([x0, x1], [y0, y1], "-o", lw=2)


n0 = Node(0, 0)
n1 = Node(1, 1)
l = Line(n0, n1)
l1 = Line(copy(n0), copy(n1))
l1.set_length(10, ref_pt="end")
l1.move(-1, -1)

fig, ax = plt.subplots()

render_line(ax, l)
render_line(ax, l1)
plt.grid()
plt.show()
