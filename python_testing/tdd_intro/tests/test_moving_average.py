import tdd_intro.moving_average as ma


def test_is_list_initialized_to_empty():
    """"Test if the data list is empty after init"""
    avg = ma.averager(3)

    assert avg.data == []


def test_number_of_points_is_zero_on_initialization():
    avg = ma.averager(3)

    assert avg.number_of_data_points == 0


def test_adding_datapoint_to_empty():
    avg = ma.averager(3)
    avg.add_data(1)

    assert avg.data == [1]
    assert avg.number_of_data_points == 1


def test_adding_datapoint_to_partially_full():
    avg = ma.averager(3)

    avg.add_data(1)
    avg.add_data(2)
    avg.add_data(3)

    assert avg.data == [1, 2, 3]
    assert avg.number_of_data_points == 3


def test_remove_first_point():
    avg = ma.averager(3)

    avg.add_data(1)
    avg.add_data(2)
    avg.add_data(3)

    avg.remove_first_point()

    assert avg.data == [2, 3]
    assert avg.number_of_data_points == 2


def test_adding_datapoint_to_full():
    avg = ma.averager(3)

    for i in range(1, 5):
        avg.add_data(i)

    assert avg.data == [2, 3, 4]
    assert avg.number_of_data_points == 3


def test_average_for_n_data_points():
    avg = ma.averager(3)
    avg.add_data(5)
    avg.add_data(7)
    avg.add_data(9)

    average = avg.running_mean()

    assert average == 7


def test_average_for_2n_data_points():
    avg = ma.averager(3)
    for i in range(1, 7):
        avg.add_data(i)

    average = avg.running_mean()

    assert average == 5


def test_average_for_n_plus_one_data_points():
        avg = ma.averager(3)
        avg.add_data(5)
        avg.add_data(7)
        avg.add_data(9)
        avg.add_data(11)

        average = avg.running_mean()

        assert average == 9
