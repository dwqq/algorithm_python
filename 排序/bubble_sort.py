#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2020/12/2 14:15 
# @File  : bubble_sort.py
# @IDE   : PyCharm
# -------------------------------


def bubble_sort(nums):
    """
    冒泡排序，依次遍历，相邻元素比较，取出最大值
    :param nums: list
    :return:
    """
    for i in range(len(nums) - 1):
        min_id = 0
        for j in range(1, len(nums) - i):
            if nums[min_id] > nums[j]:
                nums[min_id], nums[j] = nums[j], nums[min_id]
            min_id = j
    return nums


def bubble_sort2(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


if __name__ == '__main__':
    print(bubble_sort2([5, 4, 3, 2, 1, 6, 9, 7]))