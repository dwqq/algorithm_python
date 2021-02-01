#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2021/2/1 10:38 
# @File  : 砖墙.py
# @IDE   : PyCharm
# -------------------------------


def block(wall):
    """
    穿过最少的墙
    :param wall: 二维数组
    :return:
    """
    import collections
    wall_dict = collections.defaultdict(int)
    row = len(wall)
    for r in range(row):
        wall_num = 0
        for c in range(len(wall[r])-1):
            wall_num += wall[r][c]
            wall_dict[wall_num] += 1

    return row - max(wall_dict.values(), default=0)


if __name__ == '__main__':
    wall = [[1, 2, 2, 1],
            [2, 3, 1],
            [3, 3],
            [4, 2]]
    print(block(wall))