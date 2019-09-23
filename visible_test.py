import visitor


def test_get_expire_time():
    test_case = {
        (2015, 1, 31, 1): (2015, 2, 28),
        (2015, 1, 31, 3): (2015, 4, 30),
        (2015, 12, 31, 1): (2016, 1, 31),
        (2015, 11, 31, 3): (2016, 2, 29),
        (2016, 2, 29, 1): (2016, 3, 29),
        (2016, 2, 29, 1): (2016, 3, 29),
        (2016, 3, 15, 1): (2016, 4, 15),
        (2016, 3, 15, 6): (2016, 9, 15),
        (2016, 2, 29, 12): (2017, 2, 28),
    }
    for args, results in test_case.items():
        assert visitor.get_expire_day(*args) == results


def test_get_days():
    test_case = {
        (2016, 1, 1, 1): 31,
        (2016, 1, 31, 1): 29,
        (2015, 1, 31, 1): 28,
        (2015, 11, 30, 3): 91,
        (2016, 11, 30, 3): 90,
    }
    for args, results in test_case.items():
        assert visitor.get_days(*args) == results


def test_filter_array():
    test_case = [
        [[], [], []],
        [[1, 2, 3], [], [1, 2, 3]],
        [[], [1, 2, 3], []],
        [[1, 2, 3], [2], [1, 3]],
        [[1, 2, 3], [1, 3], [2]],
    ]
    for arg1, arg2, results in test_case:
        assert visitor.filter_array(arg1, arg2) == results
