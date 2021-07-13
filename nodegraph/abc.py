from abc import ABCMeta, abstractmethod


class Vertex(metaclass=ABCMeta):
    @abstractmethod
    def __bool__(self):
        ...

    @abstractmethod
    def __eq__(self, o):
        ...

    @abstractmethod
    def __lt__(self, other):
        ...


class Edge:
    ...
