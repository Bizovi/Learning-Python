import copy

'''
# objects in sets, methods:
    when you want to check if data from one source changed
# moreover, there is hash implemented by the set
# operator equality and hash
'''

class Ball(object):
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def __eq__(self, other):
        """Override the equality operator.
        INPUT:  two objects of the calss Ball
        RETURN: True if both attributes are the same
        """
        if isinstance(other, self.__class__):
            return self.color == other.color and self.size == other.size
        return False

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.color != other.color or self.size != other.size
        return False


class Box(object):
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.color == other.color and self.size == other.size
        return False

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.color != other.color or self.size != other.size
        return False


if __name__ == '__main__':
    ball1 = Ball('blue', 'small')
    ball2 = Ball('blue', 'small')
    ball3 = Ball('blue', 'big')
    # object.__lt__(self, other)  # comparation engine methods
    print(id(ball1) == id(ball2)) # False, different memory locations
    print(ball1 == ball2) # The effect of overriding the equality operator
    print(ball1 != ball2, ball2 != ball3)

    box1 = Box('blue', 'small')
    print(ball1 == box1) # True, but we don't want that -> Fix isinstance()

    # toy example with shallow copies
    a = [[1, 2, 3], [4, 5, 6]]
    b = a
    # well, fuck
    print("a before {} and b before {}".format(a, b))
    a[0][1] = 10
    print("a before {} and b before {}".format(a, b))

    # toy example of deep copies: solves the issue
    a = [[1, 2, 3], [4, 5, 6]]
    b = copy.deepcopy(a)
    print("a before {} and b before {}".format(a, b))
    a[0][1] = 10
    print("a before {} and b before {}".format(a, b))
