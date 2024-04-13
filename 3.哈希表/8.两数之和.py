#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :8.两数之和.py
# @Time     :2022/2/14 下午3:18
# @Author   :Chang Qing
 

"""
leetcode 1
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
reference：
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0001.%E4%B8%A4%E6%95%B0%E4%B9%8B%E5%92%8C.md
"""


class Solution:
    def twoSum(self, nums, target: int):
        records = dict()

        # 用枚举更方便，就不需要通过索引再去取当前位置的值
        for idx, val in enumerate(nums):
            if target - val not in records:
                records[val] = idx
            else:
                return [records[target - val], idx] # 如果存在就返回字典记录索引和当前索引