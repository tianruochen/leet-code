#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :1.子集问题.py
# @Time     :2022/3/3 下午2:19
# @Author   :Chang Qing
 

"""
leetcode 90
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出: [ [2], [1], [1,2,2], [2,2], [1,2], [] ]

思路：

做本题之前一定要先做78.子集。

这道题目和78.子集区别就是集合里有重复元素了，而且求取的子集要去重。

那么关于回溯算法中的去重问题，在40.组合总和II中已经详细讲解过了，和本题是一个套路。

剧透一下，后期要讲解的排列问题里去重也是这个套路，所以理解“树层去重”和“树枝去重”非常重要。
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0090.%E5%AD%90%E9%9B%86II.md
"""


class Solution:
    def __init__(self):
        self.paths = []
        self.path = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.backtracking(nums, 0)
        return self.paths

    def backtracking(self, nums: List[int], start_index: int) -> None:
        # ps.空集合仍符合要求
        self.paths.append(self.path[:])
        # Base Case
        if start_index == len(nums):
            return

        # 单层递归逻辑
        for i in range(start_index, len(nums)):
            if i > start_index and nums[i] == nums[i - 1]:
                # 当前后元素值相同时，跳入下一个循环，去重
                continue
            self.path.append(nums[i])
            self.backtracking(nums, i + 1)
            self.path.pop()

# 用set去重
class Solution:
    def __init__(self):
        self.answer = []
        self.answers = []
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.backtracking(nums, 0)
        return self.answers

    def backtracking(self, nums, start_index):
        self.answers.append(self.answer[:])
        used_set = set()
        for i in range(start_index, len(nums)):
            if nums[i] in used_set:
                continue
            used_set.add(nums[i])
            self.answer.append(nums[i])
            self.backtracking(nums, i+1)
            self.answer.pop()