"""This script investigates the dry-python library `returns`, which covers
* error handling in a functional style - None free code!
* optional typing
* functional programming design patterns
* more functional tools (pipelines, 'containers')
"""

from returns.result import Result, Success, Failure

def safe_divide(first: float, second: float) -> Result[float, ZeroDivisionError]:
    try:
        return Success(first / second)  # the container for success
    except ZeroDivisionError as ez:
        return Failure(ez)


if __name__ == "__main__":
    print(safe_divide(5, 0))
    print(safe_divide(5, 3))
    # print(1 + safe_divide(2, 0))

    print(Success(4).bind(lambda number: Success(number / 2)))
    print(Success(4).map(lambda number: number + 1))
    print(Success(1).unwrap())
    print(Success(0).value_or(None))
