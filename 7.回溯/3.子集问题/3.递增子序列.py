#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :3.递增子序列.py
# @Time     :2022/3/3 下午2:56
# @Author   :Chang Qing
 
"""
leetcode 491
给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

示例:

输入: [4, 6, 7, 7]
输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
说明:

给定数组的长度不会超过15。
数组中的整数范围是 [-100,100]。
给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。

看解析： 处处都能看到子集的身影，但处处是陷阱，值得好好琢磨琢磨
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0491.%E9%80%92%E5%A2%9E%E5%AD%90%E5%BA%8F%E5%88%97.md
"""


class Solution:
    def __init__(self):
        self.paths = []
        self.path = []

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        '''
        本题求自增子序列，所以不能改变原数组顺序
        '''
        self.backtracking(nums, 0)
        return self.paths

    def backtracking(self, nums: List[int], start_index: int):
        # 收集结果，同78.子集，仍要置于终止条件之前
        if len(self.path) >= 2:
            # 本题要求所有的节点
            self.paths.append(self.path[:])         # 子集问题 append后不能return

        # Base Case（可忽略）
        # if start_index == len(nums):
        #     return

        # 单层递归逻辑
        # 深度遍历中每一层都会有一个全新的usage_list用于记录本层元素是否重复使用
        usage_list = set()
        # 同层横向遍历
        for i in range(start_index, len(nums)):
            # 若当前元素值小于前一个时（非递增）或者曾用过，跳入下一循环
            if (self.path and nums[i] < self.path[-1]) or nums[i] in usage_list:
                continue
            usage_list.add(nums[i])
            self.path.append(nums[i])
            self.backtracking(nums, i + 1)
            self.path.pop()

