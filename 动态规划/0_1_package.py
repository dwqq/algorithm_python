#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2020/12/16 15:22 
# @File  : 0_1_package.py
# @IDE   : PyCharm
# -------------------------------


def backpack_record(n, c, w, v):
    """
    0-1背包问题，利用动态规划计算记录表
    :param n: list，物品种类
    :param c: int，背包容量
    :param w: list，物品质量
    :param v: list，物品价值
    :return:
    """
    rec = [[0 for _ in range(c + 1)] for _ in range(len(n) + 1)]
    for i in range(1, len(n) + 1):
        for j in range(1, c + 1):
            if j >= w[i-1]:
                rec[i][j] = max(rec[i-1][j], v[i-1] + rec[i-1][j-w[i-1]])
            else:
                rec[i][j] = rec[i-1][j]
    return rec


def backpack_results(n, c, w, res):
    """获取物品"""
    x = [False for _ in range(len(n)+1)]
    i = len(n)
    j = c
    while i >= 0:
        if res[i][j] > res[i-1][j]:
            x[i] = True
            j -= w[i-1]
        i -= 1
    for i in range(len(x)):
        if x[i]:
            print(i, end=', ')
    print()
    print('最大价值：', res[len(n)][c])


if __name__ == '__main__':
    n = ['a', 'b', 'c', 'd']
    c = 8
    w = [2, 4, 5, 3]
    v = [5, 4, 6, 2]
    res = backpack_record(n, c, w, v)
    print(res)
    backpack_results(n, c, w, res)