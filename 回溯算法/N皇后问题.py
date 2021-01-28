#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2021/1/27 18:57 
# @File  : N皇后问题.py
# @IDE   : PyCharm
# -------------------------------


def solveNQueens(n):
    """N皇后"""

    def backtrack(board, row):
        # print('row = ', row)
        if row == len(board):
            # print('row = ', row)
            res.append(board)
            print(board)
            return
        m = len(board[row])
        for col in range(m):
            # print('col = ', col)
            # print(isVaild(board, row, col))
            if isVaild(board, row, col):
                board[row][col] = 'Q'
                # print(board)
                backtrack(board, row+1)
                board[row][col] = '.'

    def isVaild(board, row, col):
        for i in range(row):
            if board[i][col] == 'Q':
                # print('is 1')
                return False
        for i in range(row):
            for j in range(len(board)):
                if board[i][j] == 'Q' and ((i-j) == (row-col) or (i+j) == (row+col)):
                    return False
        return True

    board = [['.']*n for _ in range(n)]
    res = []
    backtrack(board, 0)
    # print(res)


if __name__ == '__main__':
    solveNQueens(4)