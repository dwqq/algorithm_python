#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2020/12/2 11:33 
# @File  : select_sort.py
# @IDE   : PyCharm
# -------------------------------


def select_sort(nums):
    """
    选择排序，每次遍历选择最小的值
    :param nums: list
    :return:
    """
    res = []
    while len(nums):
        min_id = 0
        for j in range(1, len(nums)):
            if nums[min_id] > nums[j]:
                min_id = j
        res.append(nums[min_id])
        nums.pop(min_id)
    return res


def select_sort2(nums):
    for i in range(len(nums)):
        min_id = i
        for j in range(i+1, len(nums)):
            if nums[min_id] > nums[j]:
                min_id = j
        nums[min_id], nums[i] = nums[i], nums[min_id]
    return nums


if __name__ == '__main__':
    print(select_sort2([5, 4, 3, 2, 1]))
