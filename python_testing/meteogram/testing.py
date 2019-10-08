from numpy.testing import assert_almost_equal
import vcr


def get_recorder(test_file_path):
    """Return an appropriate response recorder for the given path"""
    return vcr.VCR(cassette_library_dir=str(test_file_path / 'fixtures'))
