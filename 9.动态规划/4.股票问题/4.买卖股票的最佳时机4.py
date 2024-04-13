#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :1.买卖股票的最佳时机1.py
# @Time     :2022/3/24 下午5:10
# @Author   :Chang Qing
 
"""
leetcode 188  最多可以进行k次交易

给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1： 输入：k = 2, prices = [2,4,1] 输出：2 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2。
示例 2： 输入：k = 2, prices = [3,2,6,5,0,3] 输出：7 解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4。随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。


思路：

使用二维数组 dp[i][j] ：第i天的状态为j，所剩下的最大现金是dp[i][j]

j的状态表示为：

0 还没有操作过
1 第一次买入
2 第一次卖出
3 第二次买入
4 第二次卖出
.....

大家应该发现规律了吧 ，除了0以外，偶数就是卖出，奇数就是买入。
题目要求是至多有K笔交易，那么j的范围就定义为 2 * k + 1 就可以了。
还要强调一下：dp[i][1]，表示的是第i天，买入股票的状态，并不是说一定要第i天买入股票，这是很多同学容易陷入的误区。


https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0188.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAIV.md"""

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        dp = [[0] * (2*k+1) for _ in range(len(prices))]
        for j in range(1, 2*k, 2):
            dp[0][j] = -prices[0]
        for i in range(1, len(prices)):
            for j in range(0, 2*k-1, 2):
                dp[i][j+1] = max(dp[i-1][j+1], dp[i-1][j] - prices[i])
                dp[i][j+2] = max(dp[i-1][j+2], dp[i-1][j+1] + prices[i])
        return dp[-1][2*k]

