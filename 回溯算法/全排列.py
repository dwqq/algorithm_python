#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2021/1/27 15:22 
# @File  : 全排列.py
# @IDE   : PyCharm
# -------------------------------


def all_permute(nums):
    """不重复数字全排列"""
    res = []

    def helper(new_nums, sol=[]):
        if not new_nums:
            res.append(sol)
            return
        for i in range(len(new_nums)):
            new_sol = sol + [nums[i]]
            next_nums = new_nums[0:i] + new_nums[i+1:]
            helper(next_nums, new_sol)
    
    helper(nums, [])
    return res


if __name__ == '__main__':
    print(all_permute([1, 2, 3]))

