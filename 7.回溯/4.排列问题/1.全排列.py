#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :1.全排列.py
# @Time     :2022/3/3 下午3:09
# @Author   :Chang Qing
 

"""
leetocode 46
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出: [ [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1] ]

注意：
排列问题 不需要使用startIndex 但要用一个used数组来标记用过的数字
reference:  建议
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0046.%E5%85%A8%E6%8E%92%E5%88%97.md
"""
class Solution:
    def __init__(self):
        self.path = []
        self.paths = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        因为本题排列是有序的，这意味着同一层的元素可以重复使用，但同一树枝上不能重复使用(usage_list)
        所以处理排列问题每层都需要从头搜索，故不再使用start_index
        '''
        usage_list = [False] * len(nums)
        self.backtracking(nums, usage_list)
        return self.paths

    def backtracking(self, nums: List[int], usage_list: List[bool]) -> None:
        # Base Case本题求叶子节点
        if len(self.path) == len(nums):
            self.paths.append(self.path[:])
            return

        # 单层递归逻辑
        for i in range(0, len(nums)):  # 从头开始搜索
            # 若遇到self.path里已收录的元素，跳过
            if usage_list[i] == True:
                continue
            usage_list[i] = True
            self.path.append(nums[i])
            self.backtracking(nums, usage_list)     # 纵向传递使用信息，去重
            self.path.pop()
            usage_list[i] = False