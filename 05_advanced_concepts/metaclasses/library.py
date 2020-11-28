# library.py
from dis import dis

'''
# but you don't ever use this
old_bc = __build_class__
def my_bc(fun, name, base=None, **kw):
    if base is Base:
        print('check if bar method defined')
    if base is not None:
        return old_bc(fun, name, base, **kw)
    return old_bc(fun, name, **kw)

import builtins
builtins.__build_class__= my_bc # swap class building mechanism
'''

class BaseMeta(type):
    """
    Metaclasses are classes that derive from type
    Having special methods, intercepting construction of derived types
    Rare feature, but has one clear mental models, unambiguous metaphors
    """
    def __new__(cls, name, bases, body):
        if name != 'Base' and not 'bar' in body:
            raise TypeError('bad user class')
        return super().__new__(cls, name, bases, body)

    def __init_subclass__(cls, *a, **kw):
        """Python 3.6: hook into when a subclass of a class
        Is being initialized"""
        print('init-subclass', a, kw)
        return super().__init_subclass__(*a, **kw)


class Base:
    """
    Want to make sure meatheads in the business unit
    implemented bar, else it falls appart
    You have no ability to change user code
    V1: def foo(self):
            return 'foo'

    # Python as protocol orientated language.
    # Hooks, protocols, safety valves
    # Hook into and do smth with the process of class building
    # Everything is executable runtime code.

    1. metaclasses
    2. __build_class__: hooking into classes creation protocol
    3. __init_subclass__()
    """
    def foo(self):
        return 'foo'
