#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2020/12/14 11:38 
# @File  : combine.py
# @IDE   : PyCharm
# -------------------------------


def combine(nums, sol, n):
    """
    组合
    :param nums: list
    :param sol:
    :param n:
    :return:
    """
    if n == 0:
        res.append(sol)
        return
    for i in range(len(nums)):
        new_sol = sol + [nums[i]]
        new_nums = nums[i+1:]
        combine(new_nums, new_sol, n-1)


res = []
combine([1, 2, 3, 4], [], 2)
print(res)