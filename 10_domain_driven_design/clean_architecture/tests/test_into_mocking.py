from unittest import mock
from mocking.intro_mocking import MyObj


def test_connect():
    # Setup
    external_obj = mock.Mock()

    # Exercise
    MyObj(external_obj)

    # Verify
    external_obj.connect.assert_called_with()

def test_setup():
    # Setup
    external_obj = mock.Mock()

    # Exercise
    obj = MyObj(external_obj)
    obj.setup()

    # Verify
    external_obj.setup.assert_called_with(cache=True, max_connections=256)