#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2021/1/28 19:11 
# @File  : 迷宫-最少步数.py
# @IDE   : PyCharm
# -------------------------------
def minimumMoves(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    n = len(grid)
    from collections import deque
    queue = deque([((0, 0), (0, 1), 0)])
    visited = set()

    while queue:
        pos0, pos1, step = queue.popleft()
        # print pos0, pos1
        x0, y0 = pos0
        x1, y1 = pos1
        if (x0, y0) == (n - 1, n - 2) and (x1, y1) == (n - 1, n - 1):
            return step
        if x0 == x1 and y1 > y0:# 水平
            # 向右走
            x2, y2 = x1, y1 + 1
            if 0 <= x2 < n and 0 <= y2 < n and ((x1, y1), (x2, y2)) not in visited and grid[x2][y2] != 1:
                visited.add(((x1, y1), (x2, y2)))
                queue.append(((x1, y1), (x2, y2), step + 1))
            # 向下走
            x2, y2 = x0 + 1, y0
            x3, y3 = x1 + 1, y1
            if 0 <= x2 < n and 0 <= x3 < n and 0 <= x3 < n and 0 <= y3 < n and ((x2, y2), (x3, y3)) not in visited and grid[x2][y2] != 1 and grid[x3][y3] != 1:
                visited.add(((x2, y2), (x3, y3)))
                queue.append(((x2, y2), (x3, y3), step + 1))
            # 旋转
            x2, y2 = x0 + 1, y0
            if 0 <= x2 < n and 0 <= y2 < n and ((x0, y0), (x2, y2)) not in visited and grid[x0 + 1][y0] != 1 and grid[x0 + 1][y0 + 1] != 1:
                visited.add(((x0, y0), (x2, y2)))
                queue.append(((x0, y0), (x2, y2), step + 1))

        elif x1 > x0 and y0 == y1:#竖直
            #向右走
            x2, y2 = x0, y0 + 1
            x3, y3 = x1, y1 + 1
            if 0 <= x2 < n and 0 <= x3 < n and 0 <= x3 < n and 0 <= y3 < n and ((x2, y2), (x3, y3)) not in visited and grid[x2][y2] != 1 and grid[x3][y3] != 1:
                visited.add(((x2, y2), (x3, y3)))
                queue.append(((x2, y2), (x3, y3), step + 1))
            #向下走
            x2, y2 = x1 + 1, y1
            if 0 <= x2 < n and 0 <= y2 < n and ((x1, y1), (x2, y2)) not in visited and grid[x2][y2] != 1:
                visited.add(((x1, y1), (x2, y2)))
                queue.append(((x1, y1), (x2, y2), step + 1))
            # 旋转
            x2, y2 = x0, y0 + 1
            if 0 <= x2 < n and 0 <= y2 < n and ((x0, y0), (x2, y2)) not in visited and grid[x0][y0 + 1] != 1 and grid[x0 + 1][y0 + 1] != 1:
                visited.add(((x0, y0), (x2, y2)))
                queue.append(((x0, y0), (x2, y2), step + 1))
    return -1


if __name__ == '__main__':
    grid = [[0,0,0,0,0,1],
            [1,1,0,0,1,0],
            [0,0,0,0,1,1],
            [0,0,1,0,1,0],
            [0,1,1,0,0,0],
            [0,1,1,0,0,0]]
    grid = [[0,0,1,1,1,1],
            [0,0,0,0,1,1],
            [1,1,0,0,0,1],
            [1,1,1,0,0,1],
            [1,1,1,0,0,1],
            [1,1,1,0,0,0]]
    print(minimumMoves(grid))