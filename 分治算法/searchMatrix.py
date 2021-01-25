#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2020/12/16 17:05 
# @File  : searchMatrix.py
# @IDE   : PyCharm
# -------------------------------


def search_matrix(nums, target):
    """
    二维数组查找
    :param nums: 二维数组
    :param target: 目标值
    :return:
    """
    row = len(nums)
    col = len(nums[0])

    def helper(i, j):
        if i < 0 or j > col:
            return False
        if target == nums[i][j]:
            return True
        if target > nums[i][j]:
            return helper(i, j+1)
        if target < nums[-1][0]:
            return helper(i-1, j)
    return helper(row-1, 0)


if __name__ == '__main__':
    nums = [[1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]]
    print(len(nums))
    print(len(nums[0]))
    print(nums[0])
    print(search_matrix(nums, 12))