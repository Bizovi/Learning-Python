"""Test use of the meteogram module.
Red-green refactoring pattern
"""

from meteogram import meteogram
from datetime import datetime

import numpy as np
from numpy.testing import assert_almost_equal, assert_array_almost_equal


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


#
# Exercise 1
#
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

#
# Exercise 1 - Stop Here
#

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





#
# Exercise 2 - Stop Here
#

#
# Instructor led mock example
#

#
# Exercise 3
#

#
# Exercise 3 - Stop Here
#

#
# Exercise 4 - Add any tests that you can to increase the library coverage.
# think of cases that may not change coverage, but should be tested
# for as well.
#

#
# Exercise 4 - Stop Here
#

#
# Instructor led example of image testing
#

#
# Exercise 5
#

#
# Exercise 5 - Stop Here
#

#
# Exercise 6
#

#
# Exercise 6 - Stop Here
#

#
# Exercise 7
#

#
# Exercise 7 - Stop Here
#

# Demonstration of TDD here (time permitting)
