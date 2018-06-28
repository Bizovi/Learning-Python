from functools import wraps

''' Perspective of a library developer who wants to ensure end users have
the right behavior/fix => just decorates the function. When executed it sees
thet it is decorated and goes through the function I control, i.e. the wrapper
    The opposite would be to guard against library developers changes with
unit and functional tests.
# let's say we don't want to touch a function, and to extend a functionality
# can use a decorator: needs a callable and returns a callable
'''

def p_decorate(func):
    '''Can think of it as a class extension, mutating the behavior'''
    def func_wrapper(*args, **kwargs):
        '''callable corpus, notice that it returns an enhanced version
        of the original function'''
        return "<p>{0}</p>".format(func(*args, **kwargs))
    return func_wrapper

def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper

def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper

# Important: Order is D P S
@div_decorate
@p_decorate
@strong_decorate # this gets executed first
def get_text(name):
    '''Need functools, a wrapper to keep the documentation'''
    return "Lorem ipsum, {0} dolor sit amet".format(name)

def tags(tag_name):
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
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
    print(get_text('John Snow you know nothing'))
    p1 = Person()
    print(p1.get_fullname())

    print(get_text("John"))
    print(get_text.__name__)
    print(get_text.__doc__)
    print(get_text.__module__)
