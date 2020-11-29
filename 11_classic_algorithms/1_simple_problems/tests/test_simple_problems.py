import fibonacci as fib

import hypothesis.strategies as st
from hypothesis import given


@given(n=st.integers(min_value=0, max_value=50))
def test_fibonacci_recursive(n):
    """Test algorithmic calculations with approximation to Binet's Formula
    
    Note: 
        * The naive implementation will run for an eternity
        * Binet's formula   => Sympy exact calculation, otherwise pytest.approx is useful
        * For n around 2649 => maximum recursion depth exceeded
    
    Alternative approach:
        * reference algorithmic implementation, proven correct mathematically
        * test other approaches against the reference implementation
    """
    assert fib.fib_recursive(n) == fib.binet_approx(n)


@given(n=st.integers(min_value=0, max_value=50))
def test_fibonacci_automemo(n):
    assert fib.fib_automemo(n) == fib.binet_approx(n)


@given(n=st.integers(min_value=0, max_value=3000))
def test_fibonacci_imperative(n):
    assert fib.fib_iterator(n) == fib.binet_approx(n)


@given(n=st.integers(min_value=0, max_value=3000))
def test_fibonacci_reducer(n):
    assert fib.fib_reduce(n) == fib.binet_approx(n)


@given(n=st.integers(min_value=0, max_value=10))
def test_fibonacci_generator(n):
    assert all([list(fib.fib_generator(k))[-1] == fib.binet_approx(k) for k in range(n)])
