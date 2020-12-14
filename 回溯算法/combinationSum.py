#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2020/12/14 14:12 
# @File  : combinationSum.py
# @IDE   : PyCharm
# -------------------------------


def combinationSum(nums, sum):
    """
    组合求和
    :param nums: list
    :param sum: target
    :return:
    """
    def helper(cur_sum, sol, index):
        if cur_sum > sum:
            return
        elif cur_sum == sum:
            res.append(sol)
        for i in range(index, len(nums)):
            helper(cur_sum+nums[i], sol+[nums[i]], i)

    res = []
    nums.sort()
    helper(0, [], 0)
    return res


if __name__ == '__main__':
    print(combinationSum([2, 3, 4], 8))
