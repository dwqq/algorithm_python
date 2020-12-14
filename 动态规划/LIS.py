#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2020/12/14 16:00 
# @File  : LIS.py
# @IDE   : PyCharm
# -------------------------------


def LIS(nums):
    """
    最长递增子序列
    :param nums: list
    :return:
    """
    res = [1 for _ in range(len(nums))]
    for i in range(len(nums)):
        for j in range(0, i):
            if nums[j] < nums[i]:
                res[i] = max(res[i], res[j] + 1)
    return res


if __name__ == '__main__':
    print(LIS([1, 4, 3, 4, 2, 3, 5]))