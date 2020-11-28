import pytest
from datatest import (
   working_directory
 , Select
 , validate
 , accepted
 , Missing, Extra, Deviation, Invalid
)


@pytest.fixture(scope="module")
@working_directory(__file__)
def detail():
    """Fixture for individual data"""
    return Select('country_of_birth.csv')


@pytest.fixture(scope="module")
@working_directory(__file__)
def summary():
    """Fixture for the aggregated data"""
    return Select('estimated_totals.csv')


@pytest.mark.mandatory
def test_aggregated_columns_in_individual(detail, summary):
    """Latter tests cannot pass unless data has the correct fieldnames! 
    But we accept that individual data might have more columns"""
    # Setup - fixtures
    # Exercise
    required_set = set(summary.fieldnames)

    # Validate
    with accepted(Extra):
        validate(detail.fieldnames, required_set)


def test_state_labels_contained_in_aggregate(detail, summary):
    """Individual state should be present in aggregate. 
    We can live with the missing tiny tiny commune in Aus."""
    # Setup
    requirement = summary({'state/territory'})
    ommited_territory = accepted([
        Missing('Jervis Bay Territory')
    ])

    # Exercise
    data = detail({'state/territory'})

    # Validate
    with ommited_territory:
        validate(data, requirement)


def test_population_format(detail):
    """Test that population has the right type and format"""
    # Setup - helper function
    def integer_format(x):
        return str(x).isdecimal()

    # Exercise 
    data = detail({'population'})

    # Validate
    validate(data, integer_format)


def test_population_aggregation(detail, summary):
    """Test that aggregation results in close enough numbers
    to aggregated reports for cross-check"""
    # Setup
    requirement = summary({'state/territory': 'population'}).sum()
    omitted_territory = accepted({
        'Jervis Bay Territory': Deviation(-389, 389),
        'Jervis Bay Territory': Missing(388),
    })

    # Exercise
    data = detail({'state/territory': 'population'}).sum()

    # Validate
    with accepted.percent(0.03) | omitted_territory:  # plus-minus
        validate(data, requirement)