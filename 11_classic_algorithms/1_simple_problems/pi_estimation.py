"""Various method of estimating the pi, including Leibniz formula, Buffon's needle

Note:
    This is a good opportunity to dig deeper into floating-point arithmetic
    There is an excellent course covering that from FastAI => computational linear algebra
"""

from itertools import cycle
import mpmath
from mpmath import mp
mp.prec = 30

def calculate_pi(n: int) -> float:
    """TODO(Mihai) <| Visualize the convergence as n grows, compute convergence rates
        Leibniz formula: pi ~ 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 ...
        Can split the: approximation error vs floating-point errors
    """
    numerator, denominator, operation, pi = 4.0, 1.0, 1.0, 0.0
    for _ in range(n):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
    return pi


def calculate_pi_reduce(n: int) -> float:
    """Same formula, only in functional and immutable style"""
    return sum([
        4/(den*sgn) for den, sgn in zip(range(1, n*2, 2), cycle([1, -1]))
    ])


def calculate_pi_precision(n: int) -> float:
    """Same formula, only in functional and immutable style + arbitrary precision"""
    return mpmath.fp.fsum([
        mpmath.fdiv(4, (den*sgn)) for den, sgn in zip(range(1, n*2, 2), cycle([1, -1]))
    ])