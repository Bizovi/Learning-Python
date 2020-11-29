"""Warming up with computing the fibonacci sequence with different approaches

From Classic Computer Science Problems in Python Chapter 1
Copyright 2018 David Kopec

Useful packages:
    * sympy for symbolic algebra
    * mpmath for arbitrary precision floats and rich set of functions
    * tco for implementing tail call optimization => curiosity
"""

from typing import Dict, Generator
from functools import lru_cache, reduce
import sympy

golden_ratio = sympy.S.GoldenRatio
fib_seq: Dict[int, int] = {0: 0, 1: 1}


def binet_approx(n: int) -> int:
    """The following is an exact formula, can be handled by sympy and mpmath.
    The approximation will be `phi^n / sqrt(5)`, but it results in mistakes due to floats.

    Advantages: 
        * exact, has mathematical proof
        * very efficient: O(log(n)) from power and sqrt, which are optimized
    Downsides: 
        * relies on heavy work of sympy & implemented mathematica operations
        * wouldn't work otherwise due to floating point precisions
        * not clear at the first glance where does it come from
    """
    if n < 2: return n
    return ((golden_ratio**n - (golden_ratio-1)**n) / sympy.sqrt(5)).round(0)


def fib_recursive(n: int) -> int:
    """An example of memoization, so that we don't have to compute twice. Reaches the 
    recursion limit of 1000 at around n=2600.

    Advantages:
        * Still a useful technique even in functional programming languages `let`
    Downsides:
        * Wrong method for this problem. Always can use iteration for performance
        * Not a pure function, mutates a dictionary out of the scope
        * Still hit the recursion limit.
    """
    if n not in fib_seq: 
        fib_seq[n] = fib_recursive(n - 1) + fib_recursive(n - 2)
    return fib_seq[n]


@lru_cache(maxsize=None)
def fib_automemo(n: int) -> int:
    """Implementing the mathematical definition and avoiding repeated computations

    Advantages:
        * functools.lru_cache does the heavy-lifting
        * Interpretable
    Downsides:
        * Wrong method for this problem. Always can use iteration for performance
        * Still slow and we hit the same recursion limit
        * Have to understand when lru_cache applies
    """
    if n < 2: return n
    return fib_automemo(n - 1) + fib_automemo(n - 2)


def fib_iterator(n: int) -> int:
    """The good old imperative programming does the job, with tuple unpacking"""
    if n == 0: return n
    _last, _next = 0, 1
    for _ in range(1, n):
        _last, _next = _next, _last + _next
    return _next


def fib_reduce(n: int) -> int:
    """Tuple is mapped a, b => b, a+b and initializes with 0, 1, iterated n times"""
    return reduce(
        lambda x, n: (x[1], x[0] + x[1]), range(n), (0, 1)
    )[0]


def fib_generator(n: int) -> Generator[int, None, None]:
    """A generator yielding the whole sequence"""
    yield 0
    if n > 0: yield 1

    _last, _next = 0, 1
    for _ in range(1, n):
        _last, _next = _next, _last + _next
        yield _next
