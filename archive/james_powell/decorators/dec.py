# dec.py
from inspect import getsource # getfile, getline, ...
from time import time

'''
Python is a live language: function definition runs at runtime (executable)
Suppose I want to enhance it (e.g. measure how long it runs)
Do the simplest and stupidest thing to get the job done
Then change the code in a simple function to extend the functionality
# before = time()
# result = x + y
# after  = time()
# print('Time taken', after - before)
'''

def timer(func):
    def wrap(*args, **kwargs):
        '''Wrapper function, take a common functionality,
        add some behavior to it'''
        before = time()
        result = func(*args, **kwargs)
        after  = time()
        print('elapsed', after - before)
        return result
    return wrap

def ntimes(n):
    '''
    Higher order decorators. Closure-Object duality hidden here
    Very important duality in Python
    1. Start with a Wrapper
    2. Add a function outside that constructs the decorator
    3. Decorator constructs the wrapper
    4. The wrapper wraps the function itself
    '''
    def inner(f):
        def wrap(*args, **kwargs):
            for _ in range(n):
                print('running {.__name__}'.format(f))
                result = f(*args, **kwargs)
            return result
        return wrap
    return inner

@timer # add = timer(add)
@ntimes(3)
def add(x, y = 10):
    return x + y

@timer # sub = timer(sub)
@ntimes(2)
def sub(x, y=10):
    return x - y


if __name__ == '__main__':
    print(add(20, 30)) # add('a', 'b')
    print(sub(30, 20))

    # print('Location in memory:', add)
    # print('Location in module:', add.__module__)
    # print('Argument defaults', add.__defaults__)
    # print('Function code', add.__code__.co_code)
    # print('Variable names', add.__code__.co_varnames)
    # print(getsource(add))
