"""Test use of the meteogram module.
Red-green refactoring pattern
"""

from meteogram import meteogram
from meteogram.testing import get_recorder

from datetime import datetime

import numpy as np
import pandas as pd
from pandas.testing import assert_series_equal
from numpy.testing import assert_almost_equal, assert_array_almost_equal
from unittest.mock import patch
import pytest

from pathlib import Path

recorder = get_recorder(Path(__file__).resolve().parent)


# @pytest.fixture
# def load_example_asos():
#     """
#     Fixture to load example data
#     """
#     example_data_path = Path(__file__).resolve().parent / '..' / '..' / 'staticdata'  # attribute cwd on disk
#     data_path = example_data_path / 'AMS_example_data.csv'
#
#     return meteogram.download_asos_data(data_path)



def test_degF_to_degC_at_freezing():
    """
    Test if celsius conversion is correct at freezing.
    """
    # Setup
    freezing_degF = 32.0
    freezing_degC = 0.0

    # Exercise
    result = meteogram.degF_to_degC(freezing_degF)

    # Verify, # Cleanup - none necessary
    assert result == freezing_degC



def test_title_case():
    """Test on string comparison"""
    # Setup
    in_string = "this is a test string"
    desired = "This Is A Test String"

    # Exercise
    actual = in_string.title()

    # Verify
    assert actual == desired


def test_build_asos_request_url_single_digit_datetimes():
    """Test building URL with single digit month and day."""
    # Setup
    station = "AMW"
    start_date = datetime(2019, 1, 1)
    end_date = datetime(2019, 1, 2)

    # Exercise
    result_url = meteogram.build_asos_request_url(station, start_date, end_date)

    # Verify
    truth_url = ('https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?'
        'station%5B%5D=AMW&tz=UTC&year1=2019&month1=01&day1=01&hour1=00&minute1=00'
        '&year2=2019&month2=01&day2=02&hour2=00&minute2=00&vars%5B%5D=tmpf&vars%5B%5D=dwpf'
        '&vars%5B%5D=sknt&vars%5B%5D=drct&sample=1min&what=view&delim=comma&gis=yes')
    assert result_url == truth_url


def test_build_asos_request_url_double_digit_datetimes():
    """
    Test building URL with double digit month and day.
    """
    # Setup
    station = "AMW"
    start_date = datetime(2018, 10, 11, 11)
    end_date = datetime(2018, 10, 16, 11)

    # Exercise
    result_url = meteogram.build_asos_request_url(station, start_date, end_date)

    # Verify
    truth_url = ('https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?'
        'station%5B%5D=AMW&tz=UTC&year1=2018&month1=10&day1=11&hour1=11&minute1=00'
        '&year2=2018&month2=10&day2=16&hour2=11&minute2=00&vars%5B%5D=tmpf&vars%5B%5D=dwpf'
        '&vars%5B%5D=sknt&vars%5B%5D=drct&sample=1min&what=view&delim=comma&gis=yes')
    assert result_url == truth_url


def test_does_three_equal_three():
    assert 3 == 3


def test_floating_subtraction():
    # Setup
    desired = 0.293

    # Exercise
    actual = 1 - 0.707

    # Verify
    assert abs(actual - desired) <= 0.00005
    assert_almost_equal(desired, actual)

#
# Exercise 2 - Add calculation tests here (wind components)
#
def test_wind_components():
    # Setup
    speed = np.array([10, 10, 10, 0])
    direction = np.array([0, 45, 360, 45])

    # Exercise
    u, v = meteogram.wind_components(speed, direction)
    true_u = np.array([0, -7.0710, 0, 0])
    true_v = np.array([-10, -7.0710, -10, 0])

    # Verify
    assert_array_almost_equal(true_u, u, 3)
    assert_array_almost_equal(true_v, v, 3)

def mocked_current_utc_time():
    """
    Mock the utc time function for testing with defaults.
    Allows to use decorator to switch a function with smth else in test function
    """
    return datetime(2018, 3, 26, 12)


@patch('meteogram.meteogram.current_utc_time', new=mocked_current_utc_time)
def test_that_mock_works():
    """
    Test if we really know how to use a mock
    1. what we want to replace, string
    2. what we want to replace it with
    """
    # Setup - None
    # Exercise
    result = meteogram.current_utc_time()

    # Verify
    truth = datetime(2018, 3, 26, 12)
    assert result == truth


#
# Exercise 3
#
@patch('meteogram.meteogram.current_utc_time', new=mocked_current_utc_time)
def test_build_asos_request_url_defaults():
    # Setup - none

    # Exercise
    url = meteogram.build_asos_request_url('MLI')

    # Verify
    truth = ('https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?'
        'station%5B%5D=MLI&tz=UTC&year1=2018&month1=03&day1=25&hour1=12&minute1=00&'
        'year2=2018&month2=03&day2=26&hour2=12&minute2=00&vars%5B%5D=tmpf&vars%5B%5D=dwpf&'
        'vars%5B%5D=sknt&vars%5B%5D=drct&sample=1min&what=view&delim=comma&gis=yes')
    assert url == truth


@patch('meteogram.meteogram.current_utc_time', new=mocked_current_utc_time)
def test_build_asos_request_url_default_start_only():
    """
    Test building URL with default start date.
    """
    # Setup
    end_date = datetime(2019, 3, 25, 12)

    # Exercise
    url = meteogram.build_asos_request_url('MLI', end_date=end_date)

    # Verify
    truth = ('https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?'
             'station%5B%5D=MLI&tz=UTC&year1=2019&month1=03&day1=24&hour1=12'
             '&minute1=00&year2=2019&month2=03&day2=25&hour2=12&minute2=00&'
             'vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct'
             '&sample=1min&what=view&delim=comma&gis=yes')
    assert url==truth

    # Cleanup - none required


@patch('meteogram.meteogram.current_utc_time', new=mocked_current_utc_time)
def test_build_asos_request_url_default_end_only():
    """
    Test building URL with default end date.
    """
    # Setup
    start_date = datetime(2018, 3, 24, 12)

    # Exercise
    url = meteogram.build_asos_request_url('MLI', start_date=start_date)

    # Verify
    truth = ('https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?'
             'station%5B%5D=MLI&tz=UTC&year1=2018&month1=03&day1=24&hour1=12'
             '&minute1=00&year2=2018&month2=03&day2=26&hour2=12&minute2=00&'
             'vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct'
             '&sample=1min&what=view&delim=comma&gis=yes')
    assert url==truth


def test_current_utc_time():
    # Setup - None
    # Exercise
    result = meteogram.current_utc_time()

    # Verify (result - smoke test)
    truth = datetime.utcnow()

    assert result.replace(microsecond=0) == truth.replace(microsecond=0)


# @pytest.mark.mpl_image_compare(remove_text=True)
# def test_plotting_meteogram_default(load_example_asos):
#     """The pytest will run that function, get results and pass it
#     as an argument to our function. Could be database, connection, API calls ...
#     """
#     # Setup
#     # url = meteogram.build_asos_request_url('AMW',
#     #         start_date=datetime(2018, 3, 26),
#     #         end_date=datetime(2018, 3, 27))
#
#     # need to use a fixure (common setup code)
#     # df = meteogram.download_asos_data(url) # quite bad to download from web
#     df = load_example_asos
#
#     # Exercise
#     fig, _, _, _ = meteogram.plot_meteogram(df)
#
#     # Verify - Done elsewhere
#
#     # Cleanup - none


#
# Parametrization
#
@pytest.mark.parametrize('start, end, station, expected', [
    # Single digit datetimes
    (
        datetime(2018, 1, 5, 1), datetime(2018, 1, 9, 1),
        'FSD',
        'https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?'
        'station%5B%5D=FSD&tz=UTC&year1=2018&month1=01&day1=05&hour1=01'
        '&minute1=00&year2=2018&month2=01&day2=09&hour2=01&minute2=00&'
        'vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct&'
        'sample=1min&what=view&delim=comma&gis=yes'
    ),
    # Defaults
    (None, None,
     'MLI',
     'https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?'
     'station%5B%5D=MLI&tz=UTC&year1=2018&month1=03&day1=25&hour1=12'
     '&minute1=00&year2=2018&month2=03&day2=26&hour2=12&minute2=00&'
     'vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct'
     '&sample=1min&what=view&delim=comma&gis=yes'
     ),

])
@patch('meteogram.meteogram.current_utc_time', new=mocked_current_utc_time)
def test_build_asos_requerst_url(start, end, station, expected):
    """
    Test URL building for requests, parametrized
    """
    # Setup - done by parametrized fixture

    # Exercise
    url = meteogram.build_asos_request_url(station, start, end)

    # Verify
    assert url == expected


@recorder.use_cassette('ASOS_AMW_2018032512_2018032612')
@patch('meteogram.meteogram.current_utc_time', new=mocked_current_utc_time)
def test_download_asos_data():
    """Test downloading ASOS data."""
    # Setup
    url = meteogram.build_asos_request_url('AMW')

    # Exercise
    df = meteogram.download_asos_data(url)

    # Verify
    first_row_truth = pd.Series(
                      {'station_id': 'AMW',
                       'station_name': 'Ames',
                       'latitude_deg': 41.990439,
                       'longitude_deg': -93.618515,
                       'UTC': pd.Timestamp('2018-03-25 12:00:00'),
                       'temperature_degF': 29,
                       'dewpoint_degF': 24,
                       'wind_speed_knots': 8,
                       'wind_direction_degrees': 113})

    assert_series_equal(df.iloc[0], first_row_truth)


@recorder.use_cassette('ASOS_AMW_Future')
def test_download_asos_data_in_future():
    """Test for correct behavior when asking for non-existant (future) data."""
    # Setup
    url = meteogram.build_asos_request_url('AMW',
                                           datetime(2999, 10, 10, 10),
                                           datetime(2999, 11, 10, 10))

    # Exercise
    df = meteogram.download_asos_data(url)

    # Verify
    assert df.empty

    # Cleanup - none necessary


@recorder.use_cassette('ASOS_AMW_Reversed_Dates')
def test_download_asos_data_start_after_end():
    """Test for correct behavior when start and end times are reversed."""
    # Setup
    start = datetime(2018, 8, 1, 12)
    end = datetime(2018, 7, 1, 12)
    url = meteogram.build_asos_request_url('AMW', start, end)

    # Exercise
    df = meteogram.download_asos_data(url)

    # Verify
    assert df.empty

    # Cleanup - none necessary


def test_download_asos_data_start_after_end_exception():
    """Test for correct behavior when start and end times are reversed."""
    # Setup
    start = datetime(2018, 8, 1, 12)
    end = datetime(2018, 7, 1, 12)

    # Exercise/Verify
    with pytest.raises(ValueError):
        url = meteogram.build_asos_request_url('AMW', start, end)

    # Cleanup - none necessary
