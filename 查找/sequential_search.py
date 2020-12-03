#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2020/12/3 18:55 
# @File  : sequential_search.py
# @IDE   : PyCharm
# -------------------------------


def sequential_search(nums, value):
    """
    顺序查找
    :param nums: list
    :param value: search value
    :return:
    """
    for i in range(len(nums)):
        if nums[i] == value:
            return i
    return -1


if __name__ == '__main__':
    print(sequential_search([1, 2, 3, 4, 5], 6))