#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2021/1/25 11:41 
# @File  : CoinChange.py
# @IDE   : PyCharm
# -------------------------------


def coin_change(nums, target):
    """
    利用动态规划解决凑零钱问题
    :param nums: 可选值
    :param target: 目标值
    :return:
    """
    dp = [i for i in range(target+1)]
    for i in range(len(dp)):
        for coin in nums:
            if i - coin < 0:
                continue
            else:
                dp[i] = min(dp[i], 1+dp[i-coin])
    return dp[target]


def get_combine(nums, target):
    """寻找和为target的组合"""
    def solution(cur_sum, sol, index):
        if cur_sum > target:
            return
        elif cur_sum == target:
            res.append(sol)
        for i in range(index, len(nums)):
            solution(cur_sum+nums[i], sol+[nums[i]], i)

    res = []
    nums.sort()
    solution(0, [], 0)
    res_len = [len(each_res) for each_res in res]
    min_len_index = res_len.index(min(res_len))
    return res[min_len_index]


if __name__ == '__main__':
    print(coin_change([1, 2, 5], 3))
    print(get_combine([1, 2, 5], 3))