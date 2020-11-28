import pytest
import datatest
from datatest import validate
import pandas as pd


@pytest.fixture(scope="module")
@datatest.working_directory(__file__)
def df():
    """Fixture to be reused across multiple checks"""
    return pd.read_csv("movies.csv")


@pytest.mark.mandatory
def test_column_name_validity(df):
    """Test if the critical columns are included in data
    This test is mandatory to pass"""
    # Setup - done in fixture
    # Exercise and validate
    validate(
        df.columns, # actual columns (Index object)
        {'title', 'rating', 'year', 'runtime'} # required columns
    )


def test_title_begins_with_upper_case(df):
    # Setup - done by fixture

    # Exercise - cleanup logic
    df_new = df.copy()
    df_new['title'] = df_new['title'].apply(lambda x: x.capitalize())

    # Validate
    validate.regex(df_new['title'], r'^[A-Z]')


def test_rating_perimeter_validity(df):
    """Test that the rating of movie is in the set of 
    valid ratings, for example R, G"""

    # Exercise and validate
    validate.superset(
        df['rating'],
        {'G', 'PG', 'PG-13', 'R', 'NC-17', 'GP', 'Not Rated'}
    )

    # GP, Not Rated are exceptions caught!


def test_year_is_integer(df):
    """Year should be an integer"""
    validate(df['year'], int)


def test_movie_duration_is_integer(df):
    """By convention movie duration is integer,
    Meaning minutes of runtime"""
    validate(df['runtime'], int)