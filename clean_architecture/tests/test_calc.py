import pytest
from calculator.calc import Calc


def test_add_two_numbers():
    # Setup
    c = Calc()

    # Exercise
    res = c.add(4, 5)

    # Verify
    assert res == 9


def test_add_three_numbers():
    # Setup
    c = Calc()

    # Exercise
    result = c.add(4, 5, 6)

    # Verify
    assert result == 15


def test_subtract_two_numbers():
    c = Calc()
    result = c.subtract(10, 5)
    assert result == 5


def test_multiplication_two_numbers():
    c = Calc()
    result = c.multiply(10, 5)
    assert result == 50


def test_multiplication_many_numbers():
    # Setup
    x = range(1, 10)

    # Exercise
    res = Calc().multiply(*x)

    # Verify (needs precision checks for floatss)
    assert res == 362880


def test_div_two_numbers_float():
    c = Calc()
    res = c.divide(13, 2)
    assert res == 6.5


def test_divide_by_zero_returns_inf():
    c = Calc()
    res = c.divide(14, 0)

    assert res == "inf"


def test_multiplication_by_zero_raises_exception():
    c = Calc()

    with pytest.raises(ValueError):
        c.multiply(3, 2, 0)


def test_avg_correct_average():
    c = Calc()
    res = c.avg([2, 5, 12, 98])
    assert res == 29.25


def test_avg_removes_upper_outliers():
    c = Calc()
    res = c.avg([2, 5, 12, 98], upper=90)

    assert res == pytest.approx(6.33333)


def test_avg_removes_lower_outliers():
    c = Calc()
    res = c.avg([2, 5, 12, 98], lower=10)
    assert res == pytest.approx(55)


def test_avg_upper_threshold_is_included():
    c = Calc()
    res = c.avg([2, 5, 12, 98], upper=98)

    assert res == 29.25


def test_avg_lower_threshold_is_included():
    c = Calc()
    res = c.avg([2, 5, 12, 98], lower=2)

    assert res == 29.25


def test_avg_empty_list():
    c = Calc()
    res = c.avg([])
    assert res == 0


def test_avg_manages_empty_list_after_outlier_removal():
    c = Calc()
    res = c.avg([12, 98], lower=15, upper=90)
    assert res == 0


def test_avg_manages_empty_before_after_outlier_removal():
    c = Calc()
    res = c.avg([], lower=15, upper=90)
    assert res == 0


def test_avg_manages_zero_value_lower_outlier():
    c = Calc()
    res = c.avg([-1, 0, 1], lower = 0)
    assert res == 0.5


def test_avg_manages_lower_zero_value_outlier():
    c = Calc()
    res = c.avg([-1, 0, 1], lower=0)
    assert res == 0.5


def test_avg_manages_upper_zero_value_outlier():
    c = Calc()
    res = c.avg([-1, 0, 1], upper=0)
    assert res == -0.5