#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2020/12/4 10:53 
# @File  : binary_search.py
# @IDE   : PyCharm
# -------------------------------


def binary_search(nums, target):
    """
    二分查找
    :param nums: list, 有序数组
    :param target: 目标值
    :return:
    """
    left_id, right_id = 0, len(nums)-1

    def find_mid(left_id, right_id):
        if left_id > right_id:
            return -1
        mid_id = (left_id + right_id) // 2
        if nums[mid_id] > target:
            right_id = mid_id - 1
            return find_mid(left_id, right_id)
        elif nums[mid_id] < target:
            left_id = mid_id + 1
            return find_mid(left_id, right_id)
        else:
            return mid_id

    return find_mid(left_id, right_id)


def binary_search2(nums, target):
    left_id, right_id = 0, len(nums)-1
    while left_id <= right_id:
        mid_id = (left_id+right_id) // 2
        if nums[mid_id] > target:
            right_id = mid_id - 1
        elif nums[mid_id] < target:
            left_id = mid_id + 1
        else:
            return mid_id
    return -1


if __name__ == '__main__':
    print(binary_search2([1, 2, 3, 4, 5, 6, 7, 8], 0))
