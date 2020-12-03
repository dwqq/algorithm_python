#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2020/12/3 18:26 
# @File  : bucket_sort.py
# @IDE   : PyCharm
# -------------------------------


def bucket_sort(nums):
    """
    桶排序，桶的数量固定
    :param nums: list
    :return:
    """
    max_v = max(nums)
    count_n = [0]*(max_v+1)
    res = []
    for i in nums:
        count_n[i] += 1
    for i in range(len(count_n)):
        if count_n[i]:
            res += [i]*count_n[i]
    return res


def bucket_sort2(nums):
    """
    桶的数量不固定
    :param nums:
    :return:
    """
    min_v, max_v = min(nums), max(nums)
    count_n = [0]*(max_v - min_v + 1)
    res = []
    for i in nums:
        count_n[i-min_v] += 1
    for i in range(len(count_n)):
        if count_n[i]:
            res += [i+min_v]*count_n[i]
    return res


if __name__ == '__main__':
    print(bucket_sort2([8, 6, 3, 2, 5, 7, 1, 4, 2]))