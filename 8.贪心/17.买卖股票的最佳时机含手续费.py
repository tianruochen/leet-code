#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :17.买卖股票的最佳时机含手续费.py
# @Time     :2022/3/7 下午4:37
# @Author   :Chang Qing
 

"""
leetcode 714
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

示例 1: 输入: prices = [1, 3, 2, 8, 4, 9], fee = 2 输出: 8

解释: 能够达到的最大利润: 在此处买入 prices[0] = 1 在此处卖出 prices[3] = 8 在此处买入 prices[4] = 4 在此处卖出 prices[5] = 9 总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

注意:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.

https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0714.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BA%E5%90%AB%E6%89%8B%E7%BB%AD%E8%B4%B9.md
"""

class Solution: # 贪心思路
    def maxProfit(self, prices: List[int], fee: int) -> int:
        result = 0
        minPrice = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            # 情况三：保持原有状态（因为此时买则不便宜，卖则亏本）
            elif prices[i] >= minPrice and prices[i] <= minPrice + fee:
                continue
            else: #计算利润，可能有多次计算利润，最后一次计算利润才是真正意义的卖出
                # 如果还在收获利润的区间里，表示并不是真正的卖出，而计算利润每次都要减去手续费，所以要让minPrice = prices[i] - fee;，这样在明天收获利润的时候，才不会多减一次手续费！
                result += prices[i] - minPrice - fee
                minPrice = prices[i] - fee
        return result

"""
思路与算法
换一个角度考虑，将手续费放在买入时进行计算，那么就可以得到一种基于贪心的方法。

我们用buy 表示在最大化收益的前提下，如果我们手上拥有一支股票，那么它的最低买入价格是多少。
当我们卖出一支股票时，我们就立即获得了以相同价格并且免除手续费买入一支股票的权利。

https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/solution/mai-mai-gu-piao-de-zui-jia-shi-ji-han-sh-rzlz/
"""
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        buy = prices[0] + fee
        profit = 0
        for i in range(1, n):
            if prices[i] + fee < buy:
                buy = prices[i] + fee
            elif prices[i] > buy:
                profit += prices[i] - buy
                buy = prices[i]
        return profit

