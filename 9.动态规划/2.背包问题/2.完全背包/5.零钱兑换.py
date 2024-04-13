#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :5.零钱兑换.py
# @Time     :2022/3/24 下午3:03
# @Author   :Chang Qing
 
"""
leetcode：322

给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

你可以认为每种硬币的数量是无限的。

示例 1： 输入：coins = [1, 2, 5], amount = 11 输出：3 解释：11 = 5 + 5 + 1

示例 2： 输入：coins = [2], amount = 3 输出：-1

示例 3： 输入：coins = [1], amount = 0 输出：0

示例 4： 输入：coins = [1], amount = 1 输出：1

示例 5： 输入：coins = [1], amount = 2 输出：2

提示：

1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4

思路：
动规五部曲分析如下：

1.确定dp数组以及下标的含义
dp[j]：凑足总额为j所需钱币的最少个数为dp[j]

2.确定递推公式
得到dp[j]（考虑coins[i]），只有一个来源，dp[j - coins[i]]（没有考虑coins[i]）。

凑足总额为j - coins[i]的最少个数为dp[j - coins[i]]，那么只需要加上一个钱币coins[i]即dp[j - coins[i]] + 1就是dp[j]（考虑coins[i]）

所以dp[j] 要取所有 dp[j - coins[i]] + 1 中最小的。

递推公式：dp[j] = min(dp[j - coins[i]] + 1, dp[j]);

3.dp数组如何初始化
首先凑足总金额为0所需钱币的个数一定是0，那么dp[0] = 0;

其他下标对应的数值呢？

考虑到递推公式的特性，dp[j]必须初始化为一个最大的数，否则就会在min(dp[j - coins[i]] + 1, dp[j])比较的过程中被初始值覆盖。

所以下标非0的元素都是应该是最大值。

4.确定遍历顺序
本题求钱币最小个数，那么钱币有顺序和没有顺序都可以，都不影响钱币的最小个数。

所以本题并不强调集合是组合还是排列。

如果求组合数就是外层for循环遍历物品，内层for遍历背包。
如果求排列数就是外层for遍历背包，内层for循环遍历物品。

本题钱币数量可以无限使用，那么是完全背包。所以遍历的内循环是正序

综上所述，遍历顺序为：coins（物品）放在外循环，target（背包）在内循环。且内循环正序。

5.举例推导dp数组
"""


def coinChange(self, coins: List[int], amount: int) -> int:
    dp = [amount + 1] * (amount +1)   # 考虑到要求最小值， 所以要初始化为一个比较大的数
    d[0] = 0
    for i in range(len(coins)):
        for j in range(coins[i], amount+1):
            dp[i] = min(dp[i], dp[j-coins[i]]+1)
    return dp[-1]


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''版本一'''
        # 初始化
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        # 遍历物品
        for coin in coins:
            # 遍历背包
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j - coin] + 1)
        return dp[amount] if dp[amount] < amount + 1 else -1

    def coinChange1(self, coins: List[int], amount: int) -> int:
        '''版本二'''
        # 初始化
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        # 遍历物品
        for j in range(1, amount + 1):
            # 遍历背包
            for coin in coins:
                if j >= coin:
                    dp[j] = min(dp[j], dp[j - coin] + 1)
        return dp[amount] if dp[amount] < amount + 1 else -1

