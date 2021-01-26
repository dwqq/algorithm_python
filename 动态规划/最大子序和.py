#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2021/1/26 10:21 
# @File  : 最大子序和.py
# @IDE   : PyCharm
# -------------------------------


def maxSubArray(nums):
    """最大子序和"""
    n = len(nums)
    dp = [float('-inf') for _ in range(n)]
    if n == 0:
        return 0
    dp[0] = nums[0]
    for i in range(1, n):
        dp[i] = max(nums[i], nums[i] + dp[i-1])
    return dp


if __name__ == '__main__':
    print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))