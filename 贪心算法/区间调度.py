#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2021/1/26 19:19 
# @File  : 区间调度.py
# @IDE   : PyCharm
# -------------------------------


def intervalSchedule(intvs):
    """
    区间调度问题之计算无重叠区间
    :param intvs: 区间列表，如：intvs = [[1,3], [2,4], [3,6]]
    :return:
    """
    n = len(intvs)
    intvs_sort = sorted(intvs, key=lambda x: (x[1], x[0]))
    count = 1
    end = intvs[0][1]
    for i in range(1, n+1):
        start = intvs[i-1][0]
        if end <= start:
            count += 1
            end = intvs[i-1][1]
    return count


if __name__ == '__main__':
    print(intervalSchedule([[1,3], [2,4], [3,6], [5, 7], [7, 9]]))