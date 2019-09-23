# user.py
from library import Base

# enforce a constraint on library level, fail loudly
assert hasattr(Base, 'foo'), "You broke it you fool"

class Derived(Base):
    """
    You can't do anything about library
    1. You could run a test before deploy
    2. Simpler: assertion!

    V1: def bar(self):
            return self.foo
    """
    def bar(self):
        return 'bar'


if __name__ == '__main__':
    pass
