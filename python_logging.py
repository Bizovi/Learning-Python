 # python_logging.def
import(Logging)

# debug: detailed information
# info: confirmation that things work as expected
# warining: unexpected or near future indication problems
# error: some function not running
# critical: program itself can't run

def add(x, y):
     """Add Function"""
     return  x + y

def subtract(x, y):
    """Subtract Function"""
    return x - y

def multiply(x, y):
    """Multiply Function"""
    return x * y

def divide(x, y):
    """Divide function"""
    return x / y

num1 = 10
num2 = 5

add_result = add(num1, num2)
print('Add: {} {} = {}'.format(num1, num2, add(num1, num2)))

sub_result = subtract(num1, num2)
print('Add: {} {} = {}'.format(num1, num2, subtract(num1, num2)))

mul_result = multiply(num1, num2)
print('Add: {} {} = {}'.format(num1, num2, multiply(num1, num2)))

div_result = divide(num1, num2)
print('Add: {} {} = {}'.format(num1, num2, divide(num1, num2)))
