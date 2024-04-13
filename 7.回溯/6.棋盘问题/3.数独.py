#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :3.数独.py
# @Time     :2022/3/3 下午4:37
# @Author   :Chang Qing
 

"""
37. 解数独
编写一个程序，通过填充空格来解决数独问题。

一个数独的解法需遵循如下规则： 数字 1-9 在每一行只能出现一次。 数字 1-9 在每一列只能出现一次。 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。 空白格用 '.' 表示。
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0037.%E8%A7%A3%E6%95%B0%E7%8B%AC.md
"""


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtracking(board)

    def backtracking(self, board: List[List[str]]) -> bool:
        # 若有解，返回True；若无解，返回False
        for i in range(len(board)): # 遍历行
            for j in range(len(board[0])):  # 遍历列
                # 若空格内已有数字，跳过
                if board[i][j] != '.': continue
                for k in range(1, 10):
                    if self.is_valid(i, j, k, board):
                        board[i][j] = str(k)
                        if self.backtracking(board): return True
                        board[i][j] = '.'
                # 若数字1-9都不能成功填入空格，返回False无解
                return False
        return True # 有解

    def is_valid(self, row: int, col: int, val: int, board: List[List[str]]) -> bool:
        # 判断同一行是否冲突
        for i in range(9):
            if board[row][i] == str(val):
                return False
        # 判断同一列是否冲突
        for j in range(9):
            if board[j][col] == str(val):
                return False
        # 判断同一九宫格是否有冲突
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == str(val):
                    return False
        return True