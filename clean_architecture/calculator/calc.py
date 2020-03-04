"""A module with an outrageous calculator with weird requirements 

Addition, Subtraction, Multiplication and Division.
* Division returns a float
* Division by zero returns "inf" (yikes)
* Multiplication by zero returns ValueError (yikes)
* Average of an iterable, including list
    That also cuts off values below and above thresholds (trimming)

    Typical usage example:

    from calculator.calc import Calc
    c = Calc()
    res = c.avg([2, 5, 12, 98], lower=10)
"""

from typing import (List, Dict, Tuple, Optional, Union, Collection)
from functools import reduce
from copy import deepcopy

Number = Union[int, float]


class Calc:
    def __init__(self):
        pass
    
    @staticmethod
    def add(*args: Number) -> Number:
        """Add any number of numeric values"""
        return sum(args)

    @staticmethod
    def subtract(a: Number, b: Number) -> Number:
        """Subtract two values"""
        return a - b
    
    @staticmethod
    def multiply(*args: Number) -> Number:
        """Multiply any number of values"""
        if not all(args):
            raise ValueError
        return reduce(lambda x, y: x*y, args)

    @staticmethod
    def divide(a:Number, b:Number) -> Union[Number, str]:
        """Divide two numbers in a sneaky way"""
        try: 
            return a / b
        except ZeroDivisionError:
            return "inf"

    @staticmethod
    def avg(
        it: Collection, # Sized iterable (to be indexable)
        upper: Optional[Number] = None,
        lower: Optional[Number] = None
    ) -> Number:
        """Calculate the average with option of trimming hardcoded outliers"""
        _it = deepcopy(it)

        if lower is not None:
            _it = [x for x in _it if x >= lower]

        if upper is not None:
            _it = [x for x in _it if x <= upper]

        if len(_it) < 1:
            return 0

        return sum(_it) / len(_it)