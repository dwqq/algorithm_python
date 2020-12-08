#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2020/12/7 15:24 
# @File  : merge_list.py
# @IDE   : PyCharm
# -------------------------------


def merge_list(nums1, nums2):
    """
    利用双指针实现两个数组按顺序合并
    :param nums1: 数组1
    :param nums2: 数组2
    :return:
    """
    res = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            res.append(nums1[i])
            i += 1
        else:
            res.append(nums2[j])
            j += 1
    if i == len(nums1):
        res += nums2[j:]
    elif j == len(nums2):
        res += nums1[i:]
    return res


if __name__ == '__main__':
    print(merge_list([2, 4, 6], [1, 3, 5]))