#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :3.最大子序列和.py
# @Time     :2022/3/24 下午8:36
# @Author   :Chang Qing
 

"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
示例: 输入: [-2,1,-3,4,-1,2,1,-5,4] 输出: 6 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

思路：
动规五部曲如下：

1.确定dp数组（dp table）以及下标的含义
dp[i]：包括下标i之前的最大连续子序列和为dp[i]。

2.确定递推公式
dp[i]只有两个方向可以推出来：
dp[i - 1] + nums[i]，即：nums[i]加入当前连续子序列和
nums[i]，即：从头开始计算当前连续子序列和
一定是取最大的，所以dp[i] = max(dp[i - 1] + nums[i], nums[i]);

3.dp数组如何初始化
从递推公式可以看出来dp[i]是依赖于dp[i - 1]的状态，dp[0]就是递推公式的基础。

dp[0]应该是多少呢?
根据dp[i]的定义，很明显dp[0]应为nums[0]即dp[0] = nums[0]。

4.确定遍历顺序
递推公式中dp[i]依赖于dp[i - 1]的状态，需要从前向后遍历。

举例推导dp数组
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [0] * len(nums)
        dp[0] = nums[0]
        result = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i]) #状态转移公式
            result = max(result, dp[i]) #result 保存dp[i]的最大值
        return result