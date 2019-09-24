def filter_array(target_list, filter_list):
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


def get_days(year, month, day, period=1):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0
    if month == 2 and is_run_nian(year):
        month_days[1] = 29
    total_days = month_days[month - 1] - day + 1
    for index in range(1, period):
        tmp_month = (month + index - 1) % 12 + 1
        tmp_year = year + int((month + index - 1) / 12)
        if tmp_month == 2 and is_run_nian(tmp_year):
            month_days[1] = 29
        else:
            month_days[1] = 28
        total_days += month_days[tmp_month - 1]

    end_month = (month + period - 1) % 12 + 1
    end_year = year + int((month + period - 1) / 12)
    if end_month == 2 and is_run_nian(end_year):
        month_days[1] = 29
    total_days += min(day, month_days[end_month - 1]) - 1
    return total_days
