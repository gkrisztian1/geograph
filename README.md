# NodeGraph

[![Build Status](https://travis-ci.com/gkrisztian1/nodegraph.svg?branch=main)](https://travis-ci.com/gkrisztian1/nodegraph)
[![codecov](https://codecov.io/gh/gkrisztian1/nodegraph/branch/main/graph/badge.svg?token=99DVTEL5FU)](https://codecov.io/gh/gkrisztian1/nodegraph)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Code Grade](https://www.code-inspector.com/project/25408/score/svg)](https://frontend.code-inspector.com/project/25408/dashboard)
---

## Project description

This project was created to help building parametrized 2D geometries from svg-s or dxf files or just with pure Python. After the creation you can render the
geometry with matplotlib or you can print it to a file. You can parametrize certain part of the geometry with simple commands and hence
you can solve complex geometry optimization problems. The tool detects collision and brakes the geometry into smaller parts when rendered.

## Why use?
- You can import from dxf and svg and you can add your own lines/points to the geometry.
- Easy parametrization. Color or label the parametrized object and use the set(color, parameter=value) method to modify its properties
- Easy geometry creation with repeated objects. You can spawn as many object as you want and then move them to
their destination with ease.
- You can group objects by name or color and you can do actions grouped such as translate, scale or rotate.

## Example
Let's suppose we want to optimize a shape with a FEM solver, but parts of the geometry are missing or distributed in different files. You also want to
optimize certain parts with Cubic Bézier-curves and certain parts with nodes.
```python
from nodegraph import Geometry
from nodegraph import Node


g = Geometry()
g.import_svg('resources/base.svg')
g.import_svg('resources/tail.svg')
g.import_dxf('resources/wing.dxf')

node_1 = (0, 0)
node_c1 = (5, 3)
node_c2 = (10, 4)
node_3 = (20, 0)

g.add_entity_bezier_curve(name='paramcurve1', start=node_1, c1=node_c1, c2=node_c2, end=node_3)
g.add_entity_line(name='red', x_start=4, y_start=9)


# ...
# ...

g.set('paramcurve1', c1_x = 3)


g.render()

```

## Parameter ```ptions

  - ```Node```: ``` x ```, ``` y ```
  - ```Line```: ``` x_start ```, ``` y_start ```, ``` x_end ```, ``` y_end ```
  - ```CircleArc```: ``` x_start ```, ``` y_start ```, ``` x_r ```, ``` y_r ```, ``` x_end ```, ``` y_end ```
  - ```CubicBezier```: ```x_start```, ```y_start```, ```c1_x```, ```c1_y```, ```c2_X```, ```c2_y```, ```x_end```, ```y_end```
