from abc import ABCMeta
from graphs import getid

class GrapshBaseClass(metaclass=ABCMeta):
    def __init__(self):
        self.id = getid()