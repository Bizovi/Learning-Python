 # python_logging.def
import logging
import os
import sys
import python_oop # import the classes we made before

# debug: detailed information
# info: confirmation that things work as expected
# warining: unexpected or near future indication problems (default)
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


if __name__ == "__main__":

    # part2: handlers (specific loggers) and advanced logging
    dev1 = python_oop.Developer(first='Hadley', last='Wickham', pay=90000, prog_lang='R')
    emp1 = python_oop.Employee(first='John', last='Doe', pay=50000)
    emp2 = python_oop.Manager(first='Lex', last='Luthor', pay=100000, employees=[dev1])
    print(dev1.__dict__)

    # not a good practice
    # little hack to write logs in same place
    os.chdir(sys.path[0])
    logging.basicConfig(filename='test.log', level=logging.INFO,
        format = '%(asctime)s:%(name)s:%(levelname)s:%(message)s') # constant debug=10

    num1 = 15
    num2 = 10

    add_result = add(num1, num2)
    logging.info('Add: {} {} = {}'.format(num1, num2, add(num1, num2)))
    # print('Add: {} {} = {}'.format(num1, num2, add(num1, num2)))

    sub_result = subtract(num1, num2)
    logging.info('Subtract: {} {} = {}'.format(num1, num2, subtract(num1, num2)))
    # print('Add: {} {} = {}'.format(num1, num2, subtract(num1, num2)))

    mul_result = multiply(num1, num2)
    logging.info('Multiply: {} {} = {}'.format(num1, num2, multiply(num1, num2)))
    # print('Add: {} {} = {}'.format(num1, num2, multiply(num1, num2)))

    div_result = divide(num1, num2)
    logging.info('Divide: {} {} = {}'.format(num1, num2, divide(num1, num2)))
    # print('Add: {} {} = {}'.format(num1, num2, divide(num1, num2)))
