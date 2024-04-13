#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :2.最长连续递增序列.py
# @Time     :2022/3/24 下午7:41
# @Author   :Chang Qing
 
"""
leetcode 674
给定一个未经排序的整数数组，找到最长且 连续递增的子序列，并返回该序列的长度。

连续递增的子序列 可以由两个下标 l 和 r（l < r）确定，如果对于每个 l <= i < r，都有 nums[i] < nums[i + 1] ，那么子序列 [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] 就是连续递增子序列。
示例 1： 输入：nums = [1,3,5,4,7] 输出：3 解释：最长连续递增序列是 [1,3,5], 长度为3。 尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为 5 和 7 在原数组里被 4 隔开。
示例 2： 输入：nums = [2,2,2,2,2] 输出：1 解释：最长连续递增序列是 [2], 长度为1。

思路：
1.确定dp数组（dp table）以及下标的含义
dp[i]：以下标i为结尾的数组的连续递增的子序列长度为dp[i]。
注意这里的定义，一定是以下标i为结尾，并不是说一定以下标0为起始位置。

2.确定递推公式
如果 nums[i + 1] > nums[i]，那么以 i+1 为结尾的数组的连续递增的子序列长度 一定等于 以i为结尾的数组的连续递增的子序列长度 + 1 。
即：dp[i + 1] = dp[i] + 1;

注意这里就体现出和动态规划：300.最长递增子序列的区别！
因为本题要求连续递增子序列，所以就必要比较nums[i + 1]与nums[i]，而不用去比较nums[j]与nums[i] （j是在0到i之间遍历）。
既然不用j了，那么也不用两层for循环，本题一层for循环就行，比较nums[i + 1] 和 nums[i]。
这里大家要好好体会一下！

3.dp数组如何初始化
以下标i为结尾的数组的连续递增的子序列长度最少也应该是1，即就是nums[i]这一个元素。
所以dp[i]应该初始1;

4.确定遍历顺序
从递推公式上可以看出， dp[i + 1]依赖dp[i]，所以一定是从前向后遍历。

5.举例推导dp数组
"""

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        result = 1
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]: #连续记录
                dp[i] = dp[i-1] + 1
            result = max(result, dp[i])
        return result

# 贪心
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        result = 1 #连续子序列最少也是1
        count = 1
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]: #连续记录
                count += 1
            else: #不连续，count从头开始
                count = 1
            result = max(result, count)
        return result