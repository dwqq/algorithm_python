#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2020/12/14 11:05 
# @File  : permute.py
# @IDE   : PyCharm
# -------------------------------


def permute(nums, sol=[]):
    """
    排列
    :param nums: list
    :return:
    """
    if not nums:
        res.append(sol)
        return
    for i in range(len(nums)):
        new_sol = sol + [nums[i]]
        next_nums = nums[0:i] + nums[i+1:]
        permute(next_nums, new_sol)


res = []
permute([1, 2, 3])
print(res)
