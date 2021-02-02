from typing import List

def get_empty_gezi(shudu: List[List[int]]):
    rlt = {}  # {(row, col): [int...]...}
    row, column = 0, 0
    while row < 9:
        while column < 9:
            if shudu[row][column] is not None:
                column += 1
                continue
            # 如果一个格子为None，应当是需要填入的格子
            # 获得这个格子的行，列，九宫格已经有的数字
            # 获得这个格子可能的值
            row_num_set = set(get_row_num(row, shudu))
            column_num_set = set(get_column_num(column, shudu))
            jiu_num_set = set(get_jiu_num(row, column, shudu))
            all_num_set = set(range(1, 10))
            can_set = (all_num_set.difference(row_num_set)) & (all_num_set.difference(column_num_set)) & (all_num_set.difference(jiu_num_set))
            rlt[(row, column)] = list(can_set)
            column += 1
        row += 1
        column = 0
    return rlt


def get_row_num(row, shudu):
    rlt = [data for data in shudu[row] if data is not None]
    if len(set(rlt)) != len(rlt):
        raise ValueError('执行出错')
    return rlt


def get_column_num(column, shudu):
    rlt = [data[column] for data in shudu if data[column] is not None]
    if len(set(rlt)) != len(rlt):
        raise ValueError('执行出错')
    return rlt


def get_jiu_num(row, column, shudu):
    start_row = row // 3 * 3
    start_column = column // 3 * 3
    rlt = []
    for i in range(start_row, start_row + 3):
        for j in range(start_column, start_column + 3):
            if shudu[i][j] is not None:
                rlt.append(shudu[i][j])
    if len(set(rlt)) != len(rlt):
        raise ValueError('执行出错')
    return rlt


def main():
    shudu = [
        [2, 5, None, 1, 9, None, None, None, None],
        [8, None, None, None, None, None, None, 4, None],
        [None, None, None, None, 5, None, None, 3, None],
        [None, 1, None, 5, None, 7, None, None, None],
        [None, None, 6, 8, 4, None, None, 1, None],
        [None, None, None, None, None, 3, 5, None, None],
        [7, 6, None, None, 2, None, None, None, 8],
        [None, None, None, None, None, None, None, None, None],
        [None, 8, 4, None, None, 9, 7, None, None],
    ]
    bianli_count = 0
    while bianli_count < 100:
        bianli_count += 1
        empty = get_empty_gezi(shudu)
        if len(empty) == 0:
            return shudu
        for (row, column), val in empty.items():
            if len(val) == 1:
                shudu[row][column] = val[0]
    raise ValueError('最终没实现啊')


if __name__ == "__main__":
    main()
