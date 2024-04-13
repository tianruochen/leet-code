#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :1.子集问题.py
# @Time     :2022/3/3 下午2:19
# @Author   :Chang Qing
 

"""
leetcode 78
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例: 输入: nums = [1,2,3] 输出: [ [3],   [1],   [2],   [1,2,3],   [1,3],   [2,3],   [1,2],   [] ]

思路：
求子集问题和77.组合和131.分割回文串又不一样了。

如果把 子集问题、组合问题、分割问题都抽象为一棵树的话，那么组合问题和分割问题都是收集树的叶子节点，而子集问题是找树的所有节点！

其实子集也是一种组合问题，因为它的集合是无序的，子集{1,2} 和 子集{2,1}是一样的。

那么既然是无序，取过的元素不会重复取，写回溯算法的时候，for就要从startIndex开始，而不是从0开始！

有同学问了，什么时候for可以从0开始呢？

求排列问题的时候，就要从0开始，因为集合是有序的
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0078.%E5%AD%90%E9%9B%86.md
"""

class Solution:
    def __init__(self):
        self.path = []
        self.paths = []

    def subsets(self, nums):
        self.paths.clear()
        self.path.clear()
        self.backtracking(nums, 0)
        return self.paths

    def backtracking(self, nums: List[int], start_index: int) -> None:
        # 收集子集，要先于终止判断
        self.paths.append(self.path[:])
        # Base Case
        # if start_index == len(nums):   # 这个判断可以不要
        #     return

        # 单层递归逻辑
        for i in range(start_index, len(nums)):
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()     # 回溯
