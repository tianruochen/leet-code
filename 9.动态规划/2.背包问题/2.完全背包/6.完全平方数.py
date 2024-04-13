#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :6.完全平方数.py
# @Time     :2022/3/24 下午3:13
# @Author   :Chang Qing
 

"""
leetcode 279
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

示例 1： 输入：n = 12 输出：3 解释：12 = 4 + 4 + 4

示例 2： 输入：n = 13 输出：2 解释：13 = 4 + 9

提示：

1 <= n <= 10^4

我来把题目翻译一下：完全平方数就是物品（可以无限件使用），凑个正整数n就是背包，问凑满这个背包最少有多少物品？

思路：
动规五部曲分析如下：

1.确定dp数组（dp table）以及下标的含义
dp[j]：和为j的完全平方数的最少数量为dp[j]

2.确定递推公式
dp[j] 可以由dp[j - i * i]推出， dp[j - i * i] + 1 便可以凑成dp[j]。
此时我们要选择最小的dp[j]，所以递推公式：dp[j] = min(dp[j - i * i] + 1, dp[j]);

3.dp数组如何初始化
dp[0]表示 和为0的完全平方数的最小数量，那么dp[0]一定是0。
有同学问题，那0 * 0 也算是一种啊，为啥dp[0] 就是 0呢？
看题目描述，找到若干个完全平方数（比如 1, 4, 9, 16, ...），题目描述中可没说要从0开始，dp[0]=0完全是为了递推公式。
非0下标的dp[j]应该是多少呢？
从递归公式dp[j] = min(dp[j - i * i] + 1, dp[j]);中可以看出每次dp[j]都要选最小的，所以非0下标的dp[j]一定要初始为最大值，这样dp[j]在递推的时候才不会被初始值覆盖。

4.确定遍历顺序
我们知道这是完全背包，
如果求组合数就是外层for循环遍历物品，内层for遍历背包。
如果求排列数就是外层for遍历背包，内层for循环遍历物品。
在动态规划：322. 零钱兑换中我们就深入探讨了这个问题，本题也是一样的，是求最小数！
所以本题外层for遍历背包，内层for遍历物品，还是外层for遍历物品，内层for遍历背包，都是可以的！

https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0279.%E5%AE%8C%E5%85%A8%E5%B9%B3%E6%96%B9%E6%95%B0.md
"""


class Solution:
    def numSquares(self, n: int) -> int:
        '''版本一，先遍历背包, 再遍历物品'''
        # 初始化
        nums = [i ** 2 for i in range(1, n + 1) if i ** 2 <= n]
        dp = [10 ** 4] * (n + 1)
        dp[0] = 0
        # 遍历背包
        for j in range(1, n + 1):
            # 遍历物品
            for num in nums:
                if j >= num:
                    dp[j] = min(dp[j], dp[j - num] + 1)
        return dp[n]

    def numSquares1(self, n: int) -> int:
        '''版本二， 先遍历物品, 再遍历背包'''
        # 初始化
        nums = [i ** 2 for i in range(1, n + 1) if i ** 2 <= n]
        dp = [10 ** 4] * (n + 1)
        dp[0] = 0
        # 遍历物品
        for num in nums:
            # 遍历背包
            for j in range(num, n + 1):
                dp[j] = min(dp[j], dp[j - num] + 1)
        return dp[n]
