#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :8.最接近的三数之和问题.py
# @Time     :2022/2/14 下午4:14
# @Author   :Chang Qing
 
"""
leetcode 16
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        numLen = len(nums)

        # 特殊情况的处理：数组个数小于3 及 等于 3的情况
        if numLen < 3:
            return 0
        # if numLen== 3:
        # return sum(nums)

        nums.sort()  # 数组排序
        result = []
        targetDiff = 2 ** 31 - 1  # 初始预设的最大差值

        for i in range(numLen):
            # 双指针实现
            left = i + 1
            right = numLen - 1
            while left < right:
                temp = nums[i] + nums[left] + nums[right] - target
                if temp == 0:
                    return target

                abstemp = abs(temp)
                if abstemp < targetDiff:
                    result = [i, left, right]
                    targetDiff = abstemp

                if temp > 0:
                    right = right - 1
                else:
                    left = left + 1

        return nums[result[0]] + nums[result[1]] + nums[result[2]]