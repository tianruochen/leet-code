#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :7.不同的二叉搜索树.py
# @Time     :2022/3/9 下午3:59
# @Author   :Chang Qing
 
"""
leetcode 96
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？


dp[i]定义 ：1到i为节点组成的二叉搜索树的个数为dp[i]。
递推公式：dp[i] += dp[j - 1] * dp[i - j]; ，d[j-1] 为j为头结点左子树节点数量，d[i-j] 为以j为头结点右子树节点数量

https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0096.%E4%B8%8D%E5%90%8C%E7%9A%84%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.md
"""

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[-1]