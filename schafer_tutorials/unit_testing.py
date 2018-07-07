# unit_testing.py: setup and getting started

def add(x, y):
    '''Addition function'''
    return x + y

def subtract(x, y):
    '''Subtraction function'''
    return x - y

def multiply(x, y):
    '''Subtraction function'''
    return x * y

def divide(x, y):
    '''Addition function'''
    if y == 0:
        raise  ValueError("Can't divide by zero")
    return x / y


if __name__ == '__main__':
    print(divide(2, 0))
