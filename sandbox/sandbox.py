
class A:

    def __init__(self, x, y):
        self.vec = [x, y]

    def __getattribute__(self, name: str):
        if name == 'x':
            return self.vec[0]

        elif name == 'y':
            return self.vec[1]





a = A(6, 7)

print(a.x, a.y)
