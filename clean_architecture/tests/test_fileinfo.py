from fileinfo.fileinfo import FileInfo
from unittest.mock import patch
import pytest

""" 
We know the function will use some code to get the absolute path
Within the scope of the test can repllace that and perform the test
"""

def test_init():
    filename = "somefile.ext"
    f = FileInfo(filename)
    assert f.filename == filename


def test_init_relative():
    filename = "somefile.ext"
    relative_path = f"../{filename}"
    f = FileInfo(relative_path)
    assert f.filename == filename


@patch('os.path.getsize')
@patch('os.path.abspath')
def test_get_info(abspath_mock, getsize_mock):
    # Setup
    filename = 'somefile.ext'
    original_path = f"../{filename}"

    test_abspath = 'some/abs/path'
    abspath_mock.return_value = test_abspath

    test_size = 1234
    getsize_mock.return_value = test_size

    f = FileInfo(original_path)
    assert f.get_info() == (filename, original_path, test_abspath, test_size)