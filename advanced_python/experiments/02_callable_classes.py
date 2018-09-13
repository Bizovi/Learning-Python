import socket
import sys

# Lambda and friends in functional programming: useful because they are callable
# Lambda uses callable, also used extensively in decorators
# But this is also quite dangerous


class Resolver:
    '''DNS Caching resolver version: Class implementing callable methods'''

    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        '''Such that the instance can be called as any other function'''
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache

    def clear(self):
        self._cache.clear()

    def has_host(self, host):
        return host in self._cache


# enclosures !
def sequence_class(immutable):
    # conditional expressions
    return tuple if immutable else list

# Local - Enclosure - Global - Builtin
def sort_by_last_letter(strings):
    '''Basic example of local functions, used for closures,
    keeps the state in the exterior function'''
    store = []
    def last_letter(word):
        '''Created and differs when main function is created
        Will have different memory address next time!'''
        return word[-1]
    store.append(last_letter)
    return sorted(strings, key=last_letter)

def outer():
    '''
    Outer keeps the reference, interaction with enclosing scope of
    the external function
    # semi thread-safe closure (2 thread access same memory location):
    # we should synchronise them or a catastrophe awaits
    # concurrent stuff: a thread reads x = 3 and
    # executes operations in inner function
    '''
    x = 3
    def inner(y):
        return x + y
    return inner

def raise_to(exp):
    '''Function factories and function factorization'''
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp


if __name__ == '__main__':
    resolve = Resolver()
    print(resolve('sixty-north.com')) # resolve.__call__()
    print(resolve('pluralsight.com'))
    print(resolve.__dict__)
    print('Object resolve callable? ', callable(resolve))

    seq = sequence_class(immutable=True)
    a = seq('somestringsequence')
    print(type(a))
    seq = sequence_class(immutable=False)
    a = seq('somestringsequence')
    print(type(a))

    print(sort_by_last_letter(['ghi','def','abc']))
    print(outer())

    cube = raise_to(3)
    print(cube(5))
