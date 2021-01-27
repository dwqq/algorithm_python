#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2021/1/27 10:42 
# @File  : 跳跃游戏I.py
# @IDE   : PyCharm
# -------------------------------


def canJump(nums):
    """根据数组中每个元素代表的最大跳跃位置判断能否到达最后一个位置"""
    n = len(nums)
    farthest = 0
    for i in range(n-1):
        farthest = max(farthest, i + nums[i])
        if farthest <= i:
            return False
    return farthest >= n-1


def canJump2(nums):
    """计算能跳到最后一个位置的最少跳跃次数"""
    n = len(nums)
    farthest = 0
    jumps = 0
    end = 0
    for i in range(n-1):
        farthest = max(farthest, nums[i]+i)
        if end == i:
            jumps += 1
            end = farthest
    return jumps


if __name__ == '__main__':
    print(canJump([3, 2, 1, 0, 4]))
    print(canJump([2, 3, 1, 1, 6]))
    print(canJump2([5, 3, 1, 1, 4, 5]))
    print(canJump2([2, 0, 2, 0, 1]))