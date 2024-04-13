#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :5.不同路径带障碍.py
# @Time     :2022/3/9 下午2:55
# @Author   :Chang Qing

"""
leetcode 63
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？


思路：
关键点1： 其实只要考虑到，遇到障碍dp[i][j]保持0就可以了。
关键点2： 初始化因为从(0, 0)的位置到(i, 0)的路径只有一条，所以dp[i][0]一定为1，dp[0][j]也同理。
            但如果(i, 0) 这条边有了障碍之后，障碍之后（包括障碍）都是走不到的位置了，所以障碍之后的dp[i][0]应该还是初始值0。
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0063.%E4%B8%8D%E5%90%8C%E8%B7%AF%E5%BE%84II.md
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 构造一个DP table
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]

        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0
        if dp[0][0] == 0: return 0  # 如果第一个格子就是障碍，return 0
        # 第一行
        for i in range(1, col):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = dp[0][i-1]

        # 第一列
        for i in range(1, row):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = dp[i-1][0]
        print(dp)

        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
