import pytest
import pandas as pd
from datatest import (
    working_directory,
    Select,
    validate
)

@pytest.fixture(scope="module")
@working_directory(__file__)
def users():
    return Select('users.csv')


@pytest.mark.mandatory
def test_column_validity(users):
    validate(
        users.fieldnames, 
        {'user_id', 'active'}
    )


def test_user_ids_format(users):
    """Check that user id follow a 000X format"""

    # Setup - helper function
    def _is_wellformed(x):
        return x[:-1].isdigit() and x[-1].isupper()

    # Exercise and validate
    validate(
        users('user_id'),
        _is_wellformed
    )


def test_user_active_status_is_valid(users):
    """Should be either Y or N"""
    validate(
        users({'active'}),  # the query,
        {'Y', 'N'}         # the perimeter
    )