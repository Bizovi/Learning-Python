from datatest import validate, accepted, Extra
import re


def test_data_in_requirement_set():
    """Check for set membership of a list"""
    # Setup 
    requirement = {'A', 'B'}

    # Exercise
    data = ['A', 'B', 'A']

    # Validate
    validate(data, requirement)

    # Cleanup - none needed


def test_data_validity_using_function():
    """Check data validity with a function that returns true"""
    # Setup 
    data = [2, 4, 6, 8]
    
    # Exercise
    def is_even(x):
        return x % 2 == 0

    # Validate
    validate(data, is_even)


def test_data_type_validity():
    """Test data types in a list"""
    # Setup 
    data = [0.0, 1.0, 2.9, 3.9]

    # Exercise - none needed
    # Validate
    validate(data, float)


def test_data_validity_pattern_matching():
    """Test if elements in a list match the pattern"""
    # Setup
    data = ["bake", "cake", "bake", "sake"]

    # Exercise
    regex = re.compile('[bcs]ake')

    # Validate
    validate(data, regex)


def test_list_of_tuples_types():
    """Check that tuples of values satisfy tuples of requirements"""
    # Setup
    data = [("A", 1.0), ("A", 2.0), ("B", 3.0)]

    # Exercise and validate
    requirement = ({'A', 'B'}, float)
    validate(data, requirement)


def test_dictionary_types_validity():
    """Check that values satisfy requirements of matching keys"""
    # Setup 
    data = {
        "A": 100,
        "B": 100.1,
        "C": "Sup, m8!",
        "D": [1, 2, 3]
    }

    # Exercise and validate
    requirement = {
        "A": int,
        "B": float,
        "C": str,
        "D": [1, 2, 3]
    }

    validate(data, requirement)


def test_list_with_allowed_discrepancy_in_perimeter():
    """Check for set membership. Note that failures can be:
    Extra:     data has extra elements
    Deviation: deviation from a true value
    Invalid:   not passing a condition
    Missing:   tolerance for missing data
    """
    # Setup
    data = ["A", "B", "C", "D"]

    # Exercise
    requirement = {"A", "B"}

    # Validate
    with accepted(Extra):
        validate(data, requirement)


def test_dict_with_allowed_tolerance_of_five_units():
    """Test dict fields for discrepancies and 
    accept with tolerance of 5 units"""
    # Setup
    data = {
        "A": 100,
        "B": 200,
        "C": 299,
        "D": 405
    }

    # Exercise
    requirement = {
        "A": 100,
        "B": 200,
        "C": 300,
        "D": 400
    }

    # Validate
    with accepted.tolerance(5):
        validate(data, requirement)
