# NodeGraph

[![Build Status](https://travis-ci.com/gkrisztian1/nodegraph.svg?branch=main)](https://travis-ci.com/gkrisztian1/nodegraph)
[![codecov](https://codecov.io/gh/gkrisztian1/nodegraph/branch/main/graph/badge.svg?token=99DVTEL5FU)](https://codecov.io/gh/gkrisztian1/nodegraph)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Code Grade](https://www.code-inspector.com/project/25408/score/svg)](https://frontend.code-inspector.com/project/25408/dashboard)
---

## Notes
- vertices / edges should be hashable
- prevent directly adding new edges/nodes to a graph
  - dedicated method for that
  - edges can be constructed only from the vertices that are already in the graphs vertex set.
