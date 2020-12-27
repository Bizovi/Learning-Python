import fibonacci as fib
import pi_estimation
import compression
import encription

import hypothesis.strategies as st
from hypothesis import given, example
from pytest import approx

from sympy import pi, N
from sys import getsizeof


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


@given(n=st.integers(min_value=0, max_value=30))
def test_fibonacci_automemo(n):
    assert fib.fib_automemo(n) == fib.binet_approx(n)


@given(n=st.integers(min_value=0, max_value=30))
def test_fibonacci_imperative(n):
    assert fib.fib_iterator(n) == fib.binet_approx(n)


@given(n=st.integers(min_value=0, max_value=50))
def test_fibonacci_reducer(n):
    assert fib.fib_reduce(n) == fib.binet_approx(n)


@given(n=st.integers(min_value=0, max_value=10))
def test_fibonacci_generator(n):
    assert all([list(fib.fib_generator(k))[-1] == fib.binet_approx(k) for k in range(n)])


def test_pi_estimation():
    assert abs(round(N(pi), 10) - round(pi_estimation.calculate_pi(100000), 10)) < 1e-5


def test_pi_reduce():
    assert abs(round(N(pi), 10) - round(pi_estimation.calculate_pi_reduce(int(1e5)), 10)) < 1e-5


@given(xs=st.text(st.sampled_from(["A", "C", "G", "T"])))
@example(xs="TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACC" * 100)
def test_compression_encoding_identical_decoding(xs):
    """Check invariants of compression and decompression like size perservation and id"""
    compressed = compression.CompressedGene(xs)
    assert compressed.decompress() == xs
    assert getsizeof(compressed.decompress()) == getsizeof(xs)


def test_encript_decript():
    message = "Support Vector Machines"
    key1, key2 = encription.encrypt(message)
    result: str = encription.decrypt(key1, key2)
    assert result == message 