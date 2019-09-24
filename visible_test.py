import visitor


def test_get_expire_time():
    test_case = {
        (2015, 1, 31, 1): (2015, 2, 28),
        (2015, 1, 31, 3): (2015, 4, 30),
        (2015, 12, 31, 1): (2016, 1, 31),
        (2015, 11, 31, 3): (2016, 2, 29),
        (2016, 2, 29, 1): (2016, 3, 29),
        (2016, 2, 29, 12): (2017, 2, 28),
        (2016, 3, 15, 1): (2016, 4, 15),
        (2016, 3, 15, 6): (2016, 9, 15),
        (2016, 2, 29, 12): (2017, 2, 28),
        (2016, 12, 31, 12): (2017, 12, 31),
        (2016, 12, 31, 24): (2018, 12, 31),
    }
    for args, results in test_case.items():
        print(args, results)
        assert tuple(getExpirationDate(*args)) == results


def test_get_days():
    test_case = {
        (2016, 1, 1, 1): 31,
        (2016, 1, 31, 1): 29,
        (2015, 1, 31, 1): 28,
        (2015, 11, 30, 3): 91,
        (2016, 11, 30, 3): 90,
    }
    for args, results in test_case.items():
        print(args, results)
        assert visitor.get_days(*args) == results


def test_filter_array():
    test_case = [
        [[], [], []],
        [[1, 2, 3], [], [1, 2, 3]],
        [[], [1, 2, 3], []],
        [[1, 2, 3], [2], [1, 3]],
        [[1, 2, 3], [1, 3, 3, 3, 3, 3], [2]],
        [[1, 2, 2, 2, 3], [2], [1, 3]],
        [[1, 2, 2, 2, 3], [1], [2, 2, 2, 3]],
    ]
    for arg1, arg2, results in test_case:
        print(arg1, arg2, results)
        assert list(visitor.filter_array(arg1, arg2)) == results


def is_run_nian(year):
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 == 0:
        return True
    return False


def getExpirationDate(year, month, day, period=1):
    end_year = int(year + (month + period - 1) / 12)
    end_month = (month + period - 1) % 12 + 1

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_run_nian(end_year):
        month_days[1] = 29

    end_day = min(day, month_days[end_month - 1])
    return (end_year, end_month, end_day)
