# emulating numeric types (vectors in 2D euclidian space)
from math import hypot # euclidian norm


class Vector:
    '''
    Can be extended to the multidimensional case
    Vector(2, 4) + Vector(2, 1) = Vector(4, 5)
    abs(Vector(3, 4)) = 5
    abs(Vector(3, 4) * 3) = 15
    '''
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        '''
        String representation of an object for inspection
        If possible should match the code for object creation
        Checks eval(repr(v1)) == v1 (useful for logging!)
        '''
        return 'Vector({}, {})'.format(self.x, self.y)

    def __abs__(self):
        '''Calculate the magnitude via Pythagoras in 2D'''
        return hypot(self.x, self.y)

    def __bool__(self):
        '''Return False if the magnitude of the vector is zero'''
        # bool(abs(self)) is slower
        # 0 or 5 returns 5 => 0 or 0 returns 0
        return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        '''
        Allows vector * constant but NOT constant * vector
        In order not to violate commutativity, implement __rmul__():
        '''
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == '__main__':
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    print('Sum of {} and {} is {}'.format(v1, v2, v1 + v2))
    print('{}*{}={}'.format(v1, 3, v1 * 3))

    v3 = Vector(3, 4)
    print('The magnitude of {} is {}'.format(v3, abs(v3))) # expected to be 5
    # following would be false for a null vector
    print('The magnitude of the vector {} is > 0: {}'.format(v3, bool(v3)))
