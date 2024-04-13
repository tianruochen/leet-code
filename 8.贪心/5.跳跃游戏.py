#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :5.跳跃游戏.py
# @Time     :2022/3/4 下午3:12
# @Author   :Chang Qing
 

"""
leetcode 55
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置

https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0055.%E8%B7%B3%E8%B7%83%E6%B8%B8%E6%88%8F.md
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        i = 0
        cover = 0

        # python不支持动态修改for循环中变量,使用while循环代替
        while i <= cover:
            cover = max(i + nums[i], cover)
            if cover >= len(nums) - 1: return True
            i += 1
        return False


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        cover = nums[0]
        for i in range(1, len(nums)):
            if cover < i:     # 避免第一个位置为0， 到不了第二个位置
                return False
            if cover >= len(nums) - 1:
                return True
            cover = max(cover, i + nums[i])
        # return False