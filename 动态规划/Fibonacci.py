#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2021/1/25 11:16 
# @File  : Fibonacci.py
# @IDE   : PyCharm
# -------------------------------


def fibonacci(n):
    """
    利用动态规划计算斐波那契数
    :param n: 第n个数
    :return:
    """
    dp = []
    if n < 1:
        return 0
    for i in range(n):
        if i == 0 or i == 1:
            dp.append(1)
        else:
            next_v = dp[i-1] + dp[i-2]
            dp.append(next_v)
    return dp


def fib2(n):
    """
    利用状态压缩只存储与第n个值相关的前两个值
    :param n:
    :return:
    """
    if n < 1:
        return 0
    elif n == 1 or n == 2:
        return 1
    pre, cur = 1, 1
    for i in range(3, n+1):
        pre, cur = cur, cur + pre
    return cur


if __name__ == '__main__':
    print(fibonacci(5))
    print(fib2(5))
