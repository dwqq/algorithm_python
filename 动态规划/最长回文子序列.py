#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2021/1/25 16:16 
# @File  : 最长回文子序列.py
# @IDE   : PyCharm
# -------------------------------


def longestPalindromeSubseq(s):
    """
    利用动态规划解决最长回文子序列
    :param s: 输入字符串
    :return:
    """
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]


if __name__ == '__main__':
    print(longestPalindromeSubseq('bbbababbbbbb'))