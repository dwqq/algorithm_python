#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2021/1/26 17:04 
# @File  : 零钱兑换.py
# @IDE   : PyCharm
# -------------------------------


def change(coins, amount):
    """
    用coins中的元素凑出amount的种类数
    :param coins: 列表
    :param amount: 目标值
    :return:
    """
    n = len(coins)
    dp = [[0]*(amount+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1, n+1):
        for j in range(1, amount+1):
            if j - coins[i-1] < 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
    return dp[n][amount]


if __name__ == '__main__':
    print(change([1, 2, 5], 3))