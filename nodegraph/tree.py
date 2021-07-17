
class Tree:
    def __init__(self):
        self.vec = list()

    def insert(self, val):
        try:
            idx = self.vec.index(val)
            return self.vec[idx]
        except ValueError:
            self.vec.append(val)
            return val



    def __iter__(self):
        yield from self.vec
