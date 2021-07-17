from uuid import uuid4
from time import perf_counter
from functools import wraps

def getID():
    return int(uuid4())

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = perf_counter()
        result = f(*args, **kw)
        te = perf_counter()
        print(f'function: {f.__name__} took: {te-ts:2.5f} sec.')
        return result
    return wrap
