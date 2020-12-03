#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2020/12/3 16:57 
# @File  : shell_sort.py
# @IDE   : PyCharm
# -------------------------------


def shell_sort(nums):
    """
    希尔排序
    :param nums: list
    :return:
    """
    step = len(nums) // 2
    while step:
        for i in range(step, len(nums)):
            ind = i
            while ind >= step and nums[ind] < nums[ind-step]:
                nums[ind], nums[ind-step] = nums[ind-step], nums[ind]
                ind -= step
        step //= 2
    return nums


if __name__ == '__main__':
    print(shell_sort([5, 3, 6, 2, 4, 1, 7]))