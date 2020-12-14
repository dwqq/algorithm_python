#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2020/12/14 15:25 
# @File  : goUpStairs.py
# @IDE   : PyCharm
# -------------------------------


def go_up_stairs(n):
    """
    动态规划解决爬楼梯问题
    :param n: int, n层楼梯
    :return:
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    next_s = [1, 2]
    for i in range(2, n):
        next_s.append(next_s[i-1] + next_s[i-2])
    return next_s


if __name__ == '__main__':
    print(go_up_stairs(10))