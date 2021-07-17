# NodeGraph

[![Build Status](https://travis-ci.com/gkrisztian1/nodegraph.svg?branch=main)](https://travis-ci.com/gkrisztian1/nodegraph)

---

## Notes
- vertices / edges should be hashable
- prevent directly adding new edges/nodes to a graph
  - dedicated method for that
  - edges can be constructed only from the vertices that are already in the graphs vertex set.
