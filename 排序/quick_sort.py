#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2020/12/3 11:18 
# @File  : quick_sort.py
# @IDE   : PyCharm
# -------------------------------


def quick_sort(nums):
    """
    快速排序，选取基准，将其余值按大于或小于基准分列左右，递归获得排序的列表
    :param nums: list
    :return:
    """
    if len(nums) <= 1:
        return nums
    key = nums[0]
    left_list, right_list, mid_list = [], [], [key]
    print('mid_list: ', mid_list)
    for i in range(1, len(nums)):
        print('循环：', i)
        if nums[i] < key:
            left_list.append(nums[i])
            print('left_list: ', left_list)
        elif nums[i] > key:
            right_list.append(nums[i])
            print('right_list: ', right_list)
        else:
            mid_list.append(nums[i])
    res = quick_sort(left_list) + mid_list + quick_sort(right_list)
    print('res: ', res)
    return res


if __name__ == '__main__':
    print(quick_sort([5, 4, 6, 8, 3, 2, 7, 1]))