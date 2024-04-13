#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :1.最长递增子序列.py
# @Time     :2022/3/24 下午7:31
# @Author   :Chang Qing
 

"""
leetcode 300
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
示例 1： 输入：nums = [10,9,2,5,3,7,101,18] 输出：4 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
示例 2： 输入：nums = [0,1,0,3,2,3] 输出：4
示例 3： 输入：nums = [7,7,7,7,7,7,7] 输出：1

思路：
1.dp[i]的定义
dp[i]表示i之前包括i的以nums[i]结尾最长上升子序列的长度

2.状态转移方程
位置i的最长升序子序列等于j从0到i-1各个位置的最长升序子序列 + 1 的最大值。
所以：if (nums[i] > nums[j]) dp[i] = max(dp[i], dp[j] + 1);
注意这里不是要dp[i] 与 dp[j] + 1进行比较，而是我们要取dp[j] + 1的最大值。

3.dp[i]的初始化
每一个i，对应的dp[i]（即最长上升子序列）起始大小至少都是1.

4.确定遍历顺序
dp[i] 是有0到i-1各个位置的最长升序子序列 推导而来，那么遍历i一定是从前向后遍历。

reference：
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0300.%E6%9C%80%E9%95%BF%E4%B8%8A%E5%8D%87%E5%AD%90%E5%BA%8F%E5%88%97.md
"""
# 一个数组的子序列问题 for循环都从1开始

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        dp = [1] * len(nums)
        result = 0
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            result = max(result, dp[i])     # 取长的子序列
        return result
