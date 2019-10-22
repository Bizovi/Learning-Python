import pytest
import datatest as dt
from pprint import pprint

# big advantage is in lazy evaluation
select = dt.Select('example.csv')


def uppercase(value):
    return str(value).upper()


def not_z(value):
    return value != "z"


if __name__ == "__main__":
    print("Column names: ", select.fieldnames)
    print("First column: ", select(['A']).fetch())
    print("Unique values: ", select({'A'}).fetch())

    pprint(select(("A", "B")).fetch())
    pprint(select({('A', 'B'): ['C']}).fetch(), width=1)

    pprint(select("A", B='foo').fetch())
    print(select([('A', 'B', 'C')], A='y', B='bar').fetch())

    pprint(select({('A', 'B'): 'C'}).sum().fetch(), width=1)
    print(select('A').map(uppercase).fetch())

    print(select('A').filter(not_z).fetch())