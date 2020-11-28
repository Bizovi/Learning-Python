# Py data model, means by which you can implement protocols with meaning for objects
# Dunder implements the protocol, high level sintax invokes the protocol
# e.g. .()   ->   __call__

# Protocol view of python
# Builtin inheritance protocol
# Caviards around OOP in python

class Polynomial:
    """
    Some behavior I want to implement, write data model methods
    Pattern: Top level function (syntax): corresponding __fun__
    """
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        """Delegate back to the protocol itself"""
        return len(self.coeffs)

    def __call__(self):
        pass


if __name__ == '__main__':
    p1 = Polynomial(1, 2, 3) # 3
    p2 = Polynomial(*(3, 4, 3)) # 3x^2 + 4x + 3

    print(p1.__dict__)
    print(p2.__dict__)
    print(p1)

    print(p1 + p2)
    print(len(p1))
