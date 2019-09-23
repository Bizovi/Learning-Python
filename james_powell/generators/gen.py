# gen.py
from time import sleep

'''
There's more to it than eagerness vs laziness divide. There is smth more
fundamental.
EAGER: library code ran to completion and returned the RESULT to user
Generative (core conceptualization between generators):
    little bit of library code ran -> user code ran
    little bit of library code ran -> user code ran
    little bit of library code ran -> user code ran

# IDEA of Subroutines (exec code that runs to completion)
# one entry and exit point

# Top level sintax -> underscore method (ABSOLUTELY KEY)
#   .()     ->  __call__
'''

def add(x, y):
    return x + y

class Adder:
    """
    Difference appears if we want stateful behavior
    # def __init__(self):
    #         self.z = 0
    # def __call__(self, x, y):
    #     self.z = self.z + 0 # + 1
    #     return x + y + self.z
    """
    def __call__(self, x, y):
        return x + y

add_cls = Adder()

# let's think of a function that takes a lot of time to do something
def compute():
    """
    Eager:
        this function, irrespectively of what you care in this
        computation, always takes same memory and time
    Better way?
    """
    rows = []
    for i in range(10):
        sleep(.5)
        rows.append(i)
    return rows


class Compute:
    """
    For the class to be iterated over, we need to implement __methods__
    # xj = iter(xs)       -> __iter__
    # while True:
    #     x = next(xj)    -> __next__
    """
    def __call__(self):
        """Returns list of all values"""
        rows = []
        for i in range(10):
            sleep(.5)
            rows.append(i)
        return rows

    def __iter__(self):
        self.last = 0
        return self

    def __next__(self):
        """
        Returns a single (last) value
        Ugly, hard to read, there is much nicer ways to write this
        And this is what a GENERATOR is
        """
        rows = self.last # captures the last value we looked at
        self.last += 1   # increments it
        if self.last > 10:
            raise StopIteration()
        sleep(.5)
        return rows

def compute2():
    """Function that doesn't return eagerly:
    1. no storage
    2. return values as you see
    """
    for i in range(10):
        sleep(.5)
        yield i


class Api:
    """
    Everything blows up if you don't run in order
    Generative computation yields RESULT and CONTROL back to the caller
    They want to make sure we mix code in the right order (library <> user)
    """
    def run_this_first(self):
        first()
    def run_this_second(self):
        second()
    def run_this_last(self):
        last()

def api():
    """
    ENFORCE SEQUENCING:
        generator runs up to first(), no value, but yields control
        caller can resume
        caller can resume
    Can guarantee that the last wasn't called befor second and first methods
    Ultimately coroutine enabling interleaving
    """
    first()
    yield
    second()
    yield
    last()


if __name__ == '__main__':
    print(add(20, 15))
    print(add_cls(20, 15))
    # print(compute())
    # print(compute2())

    # no storage anymore, can do faster stuff with it, one by one
    # for val in Compute():
    #     print(val)
    print(compute2()) # returns a GENERATOR
