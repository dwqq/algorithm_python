#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2021/1/26 17:59 
# @File  : 分割等和子集.py
# @IDE   : PyCharm
# -------------------------------


def canPartition(nums):
    """将nums分割为和相等的两个子集"""
    n = len(nums)
    if sum(nums) % 2 != 0:
        return False
    sum_mid = sum(nums) // 2
    dp = [[False]*(sum_mid+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True
    for i in range(1, n+1):
        for j in range(1, sum_mid+1):
            if j - nums[i-1] < 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
    return dp[n][sum_mid]


if __name__ == '__main__':
    print(canPartition([1, 5, 11, 5]))