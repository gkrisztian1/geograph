from abc import ABCMeta, abstractmethod

class GeometryPiece(metaclass=ABCMeta):
    tol = 1e-3

    def __bool__(self):
        return True

    @abstractmethod
    def set(self, *args, **kwargs):
        ...

class Vertex(metaclass=ABCMeta):

    @abstractmethod
    def __bool__(self):
        ...

    @abstractmethod
    def __eq__(self, o):
        ...


class Edge:
    ...
