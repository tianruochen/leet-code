#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :2.最长回文子序列.py
# @Time     :2022/3/24 下午9:41
# @Author   :Chang Qing
 
"""
leetcode 516
给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。
示例 1: 输入: "bbbab" 输出: 4 一个可能的最长回文子序列为 "bbbb"。
示例 2: 输入:"cbbd" 输出: 2 一个可能的最长回文子序列为 "bb"。

https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0516.%E6%9C%80%E9%95%BF%E5%9B%9E%E6%96%87%E5%AD%90%E5%BA%8F%E5%88%97.md
"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # dp[i][j]：字符串s在[i, j]范围内最长的回文子序列的长度为dp[i][j]。
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]