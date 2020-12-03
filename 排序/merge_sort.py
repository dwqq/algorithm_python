#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2020/12/2 14:42 
# @File  : merge_sort.py
# @IDE   : PyCharm
# -------------------------------


def merge_sort(num):
    if len(num) <= 1:
        return num
    mid = int(len(num)/2)
    llist, rlist = merge_sort(num[:mid]), merge_sort(num[mid:])
    print('llist: ', llist)
    print('rlist: ', rlist)
    result = []
    i, j = 0, 0
    while i < len(llist) and j < len(rlist):
        if rlist[j]<llist[i]:
            result.append(rlist[j])
            j += 1
        else:
            result.append(llist[i])
            i += 1
    result += llist[i:]+rlist[j:]
    print('result: ', result)
    return result


def merge_sort2(nums):
    """
    归并排序，递归二分拆分，最小单元排序，最后合并
    :param nums: list
    :return:
    """
    if len(nums) <= 1:
        return nums
    mid_num = int(len(nums)/2)
    left_list, right_list = merge_sort2(nums[:mid_num]), merge_sort2(nums[mid_num:])
    res = []
    i, j = 0, 0
    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            res.append(left_list[i])
            i += 1
        else:
            res.append(right_list[j])
            j += 1
    res += left_list[i:] + right_list[j:]
    return res


if __name__ == '__main__':
    result = merge_sort2([5,3,9,6,1,2,8,7])
    print(result)
