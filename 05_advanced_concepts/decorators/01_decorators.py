from typing import Callable
from functools import wraps

""" Imagine you're a library developer who wants to ensure end users have
the right behavior/fix => just decorate the function. 
When executed, it goes through the function I control, i.e. the wrapper.
The opposite would be to guard against library developers changes with
unit and functional tests.
# let's say we don't want to touch a function, and to extend a functionality
# can use a decorator: takes a callable and returns a callable
"""

def p_decorate(func: Callable) -> Callable:
    """Can think of it as a class extension, mutating the behavior
    of the original function"""

    def func_wrapper(*args, **kwargs) -> str:
        """Callable corpus, notice that it returns an enhanced version
        of the original function.
        
        Arguments:
        ----------
        args: capturing the positional arguments of original function
        kwargs: capturing the named arguments of original function
        """
        return f"<p>{func(*args, **kwargs)}</p>"
    return func_wrapper


def strong_decorate(func: Callable) -> Callable:
    """Make a html <strong> tag out of a string"""
    def func_wrapper(name: str) -> str:
        return f"<strong>{func(name)}</strong>"
    return func_wrapper


def div_decorate(func: Callable) -> Callable:
    """Make a html <div> tag out of a string"""
    def func_wrapper(name: str) -> str:
        return f"<div>{func(name)}</div>"
    return func_wrapper


# Important: Order is D P S
@div_decorate # this gets executed first
@p_decorate
@strong_decorate 
def get_text_(name: str) -> str:
    """Need `functools.wrapper` to keep the documentation"""
    return f"Lorem ipsum, {name} dolor sit amet"


def tags(tag_name: str) -> Callable:
    """Parametrized decorator that perserves docs"""
    def tags_decorator(func: Callable) -> Callable:
        @wraps(func)
        def func_wrapper(name: str) -> Callable:
            return f"<{tag_name}>{func(name)}</{tag_name}>"
        return func_wrapper
    return tags_decorator


# CHECK WHEN AND WHERE IT LOSES DOCS AND ATTRIBUTES
@tags("p")
def get_text(name):
    """returns some text"""
    return "Hello " + name


class Person:
    def __init__(self):
        self.name = 'John'
        self.family = 'Snow'

    @p_decorate
    def get_fullname(self):
        return self.name + ' ' + self.family


if __name__ == '__main__':
    print(get_text_('John Snow you know nothing'))

    p1 = Person()
    print(p1.get_fullname())

    print(get_text("John"))
    print(get_text.__name__)
    print(get_text.__doc__)
    print(get_text.__module__)
