#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2020/12/11 14:12 
# @File  : MaxAreaOfIsland.py
# @IDE   : PyCharm
# -------------------------------


def max_area_of_island(grid):
    """
    寻找最大岛屿面积，二维
    :param grid: 区域网格，值为1说明为岛屿，值为0说明为海
    :return:
    """
    row = len(grid)
    col = len(grid[0])
    # 记录是否到达过该位置
    arrived = [[False for j in range(col)] for i in range(row)]
    ans = 0

    def DFS(x, y):
        """深度优先遍历"""
        if 0 <= x < row and 0 <= y < col and not arrived[x][y] and grid[x][y] == 1:
            arrived[x][y] = True
            return 1 + DFS(x-1, y) + DFS(x+1, y) + DFS(x, y-1) + DFS(x, y+1)
        else:
            return 0

    for i in range(row):
        for j in range(col):
            area = DFS(i, j)
            if area > ans:
                ans = area
    return ans


if __name__ == '__main__':
    grid_test = [[0, 0, 0, 0, 1, 1, 0],
                 [0, 1, 1, 0, 1, 1, 0],
                 [0, 1, 1, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 1, 1],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 1]]
    print(max_area_of_island(grid_test))
