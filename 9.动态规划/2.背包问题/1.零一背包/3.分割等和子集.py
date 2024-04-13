#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :3.分割等和子集.py
# @Time     :2022/3/23 下午7:51
# @Author   :Chang Qing
 
"""
leetcode 416

给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
注意: 每个数组中的元素不会超过 100 数组的大小不会超过 200

示例 1: 输入: [1, 5, 11, 5] 输出: true 解释: 数组可以分割成 [1, 5, 5] 和 [11].
示例 2: 输入: [1, 2, 3, 5] 输出: false 解释: 数组不能分割成两个元素和相等的子集.

提示：

1 <= nums.length <= 200
1 <= nums[i] <= 100

动规五部曲分析如下：

1.确定dp数组以及下标的含义
01背包中，dp[j] 表示： 容量为j的背包，所背的物品价值可以最大为dp[j]。

套到本题，dp[j]表示 背包总容量是j，最大可以凑成j的子集总和为dp[j]。

2.确定递推公式
01背包的递推公式为：dp[j] = max(dp[j], dp[j - weight[i]] + value[i]);

本题，相当于背包里放入数值，那么物品i的重量是nums[i]，其价值也是nums[i]。

所以递推公式：dp[j] = max(dp[j], dp[j - nums[i]] + nums[i]);

3.dp数组如何初始化
在01背包，一维dp如何初始化，已经讲过，

从dp[j]的定义来看，首先dp[0]一定是0。

如果如果题目给的价值都是正整数那么非0下标都初始化为0就可以了，如果题目给的价值有负数，那么非0下标就要初始化为负无穷。

这样才能让dp数组在递归公式的过程中取的最大的价值，而不是被初始值覆盖了。

本题题目中 只包含正整数的非空数组，所以非0下标的元素初始化为0就可以了。
4.确定遍历顺序
在动态规划：关于01背包问题，你该了解这些！（滚动数组）中就已经说明：如果使用一维dp数组，物品遍历的for循环放在外层，遍历背包的for循环放在内层，且内层for循环倒序遍历！
5.举例推导dp数组
dp[j]的数值一定是小于等于j的。

如果dp[j] == j 说明，集合中的子集总和正好可以凑成总和j，理解这一点很重要。

reference:
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0416.%E5%88%86%E5%89%B2%E7%AD%89%E5%92%8C%E5%AD%90%E9%9B%86.md
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        taraget = sum(nums)
        if taraget % 2 == 1: return False
        taraget //= 2
        dp = [0] * 10001
        for i in range(len(nums)):
            for j in range(taraget, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
        return taraget == dp[taraget]