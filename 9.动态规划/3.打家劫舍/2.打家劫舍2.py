#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :2.打家劫舍2.py
# @Time     :2022/3/24 下午4:33
# @Author   :Chang Qing
 

"""
leetcode 213
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。

示例 1：
输入：nums = [2,3,2] 输出：3 解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2： 输入：nums = [1,2,3,1] 输出：4 解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。偷窃到的最高金额 = 1 + 3 = 4 。
示例 3： 输入：nums = [0] 输出：0

提示：
1 <= nums.length <= 100
0 <= nums[i] <= 1000

https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0213.%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8DII.md
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        #在198入门级的打家劫舍问题上分两种情况考虑
        #一是不偷第一间房，二是不偷最后一间房
        if len(nums)==1:#题目中提示nums.length>=1,所以不需要考虑len(nums)==0的情况
            return nums[0]
        val1=self.robRange(nums[1:])#不偷第一间房
        val2=self.robRange(nums[:-1])#不偷最后一间房
        return max(val1,val2)

    def robRange(self,nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]