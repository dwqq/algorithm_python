#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2020/11/30 17:16 
# @File  : insert_sort.py
# @IDE   : PyCharm
# -------------------------------


def insert_sort(nums):
    """
    插入排序，依次选择元素进行排序
    :param nums: list
    :return:
    """
    res = []
    for i in range(len(nums)):
        if len(res) == 0:
            res.append(nums[i])
            continue
        for j in range(len(res)):
            if res[j] > nums[i]:
                res.insert(j, nums[i])
                break
            elif res[-1] <= nums[i]:
                res.append(nums[i])
                break
    return res


def insert_sort2(nums):
    if len(nums) == 0:
        return nums
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] > nums[i]:
                insert_value = nums[i]
                nums.pop(i)
                nums.insert(j, insert_value)
                break
    return nums


if __name__ == '__main__':
    print(insert_sort2([3, 2, 5, 7, 4, 1, 6]))
