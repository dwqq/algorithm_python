#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2021/2/1 11:09 
# @File  : 最多重复次数.py
# @IDE   : PyCharm
# -------------------------------


def max_repeat(nums):
    """数组中重复次数最多元素的重复次数"""
    import collections
    nums_dict = collections.defaultdict(int)
    for num in nums:
        nums_dict[num] += 1
    return max(nums_dict.values(), default=0)


if __name__ == '__main__':
    print(max_repeat([1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 2, 3, 3]))