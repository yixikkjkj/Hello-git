def filter_array(target_list, filter_list):
    # [], []
    # [1, 2, 3], []
    # [], [1, 2, 3]
    # [1, 2, 3], [2]
    # [1, 2, 3], [1, 3]
    i, j = 0, 0
    result_list = []
    while i < len(target_list) and j < len(filter_list):
        if target_list[i] < filter_list[j]:
            result_list.append(target_list[i])
            i += 1
        elif target_list[i] == filter_list[j]:
            i += 1
        else:
            j += 1
    if j >= len(filter_list):
        result_list.extend(target_list[i:])

    return result_list


def is_run_nian(year):
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 == 0:
        return True
    return False


def get_expire_day(year, month, day, period=1):
    end_year = int(year + (month + period - 1) / 12)
    end_month = (month + period - 1) % 12 + 1

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_run_nian(end_year):
        month_days[1] = 29
    
    end_day = min(day, month_days[end_month - 1])
    return (end_year, end_month, end_day)


if __name__ == "__main__":
    get_expire_day(2016, 1, 31, 1)
