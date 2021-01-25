#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2021/1/25 18:01 
# @File  : minDistance.py
# @IDE   : PyCharm
# -------------------------------


def minDistance(s1, s2):
    """
    利用动态规划解决编辑距离问题，将s1通过最少操作变为s2
    :param s1:
    :param s2:
    :return:
    """
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        dp[i][0] = i
    for j in range(1, n+1):
        dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
    return dp[m][n]


if __name__ == '__main__':
    print(minDistance('rad', 'apple'))