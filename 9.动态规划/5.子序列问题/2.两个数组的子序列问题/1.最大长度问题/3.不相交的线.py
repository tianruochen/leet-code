#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :3.不相交的线.py
# @Time     :2022/3/24 下午8:04
# @Author   :Chang Qing
 

"""
leetcode 1035
我们在两条独立的水平线上按给定的顺序写下 A 和 B 中的整数。
现在，我们可以绘制一些连接两个数字 A[i] 和 B[j] 的直线，只要 A[i] == B[j]，且我们绘制的直线不与任何其他连线（非水平线）相交。
以这种方法绘制线条，并返回我们可以绘制的最大连线数。

思路：

相信不少录友看到这道题目都没啥思路，我们来逐步分析一下。
绘制一些连接两个数字 A[i] 和 B[j] 的直线，只要 A[i] == B[j]，且直线不能相交！
直线不能相交，这就是说明在字符串A中 找到一个与字符串B相同的子序列，且这个子序列不能改变相对顺序，只要相对顺序不改变，链接相同数字的直线就不会相交。
其实也就是说A和B的最长公共子序列是[1,4]，长度为2。 这个公共子序列指的是相对顺序不变（即数字4在字符串A中数字1的后面，那么数字4也应该在字符串B数字1的后面）
这么分析完之后，大家可以发现：本题说是求绘制的最大连线数，其实就是求两个字符串的最长公共子序列的长度！

https://github.com/youngyangyang04/leetcode-master/blob/master/problems/1035.%E4%B8%8D%E7%9B%B8%E4%BA%A4%E7%9A%84%E7%BA%BF.md
"""

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = [[0] * (len(B)+1) for _ in range(len(A)+1)]
        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]