#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2020/12/16 11:47 
# @File  : getChange.py
# @IDE   : PyCharm
# -------------------------------


def get_change(nums, target):
    """
    硬币找零问题
    :param nums: list, 硬币类型
    :param target: 目标钱数
    :return:
    """
    nums.sort()
    i = len(nums) - 1
    while i >= 0:
        if target >= nums[i]:
            n = int(target // nums[i])
            target -= n*nums[i]
            print(n, nums[i])
        i -= 1


if __name__ == '__main__':
    get_change([0.05,0.1,0.2,0.5,1.0,2.0], 10.5)
    get_change([1, 3, 4], 6)