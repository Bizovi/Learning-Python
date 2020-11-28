from property_testing import quickstart as qs

import hypothesis 
from hypothesis.strategies._internal.core import lists
from hypothesis import given, example, note, assume
import hypothesis.strategies as st

from math import isnan


def test_encoding_old_way():
    result = qs.encode("Hello")

    assert result[0][1] == 1
    assert result[0][0] == 'H'
    assert result[2][0] == 'l'
    assert result[2][1] == 2


@given(st.text())
@example(s="")
def test_decode_inverts_encode(s):
    assert qs.decode(qs.encode(s)) == s


@given(st.integers(), st.integers())
def test_integers_are_commutative(x, y):
    assert x + y == y + x
    assert (x + y) - y == x


@given(st.lists(st.integers()))
def test_reversing_twice_gives_same_list(xs):
    ys = list(xs)
    ys.reverse()
    ys.reverse()

    assert xs == ys


@given(st.tuples(st.booleans(), st.text()))
def test_look_tuples_work_too(t):
    assert len(t) == 2
    assert isinstance(t[0], bool)
    assert isinstance(t[1], str)


@given(st.lists(st.integers()), st.randoms(use_true_random=False))
def test_shuffle_is_noop(ls, r):
    """Example of displaying additional output"""
    ls2 = list(ls)
    r.shuffle(ls2)
    note(f"Shuffle: {ls2=}")  # include the result at the end of the run
    assert len(ls) == len(ls2)


@given(st.integers().filter(lambda x: x % 2 == 0))
def test_even_integers(x):
    assert x % 2 == 0


@given(st.floats())
def test_negation_is_self_inverse_for_non_nan(x):
    """Prevents hypothesis to get stuck on some example we don't want to with assume()
    Details the assumptions over the generated inputs
    """
    assume(not isnan(x))
    assert x == -(-x)


@given(st.lists(st.integers(min_value=1, max_value=1000)))
def test_sum_is_positive(xs):
    assume(len(xs) > 1)
    # assume(all(1 <= x <= 1000 for x in xs))
    # assume(all(x > 0 for x in xs))
    assert sum(xs) > 0