#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :4.组合之和2.py
# @Time     :2022/3/2 下午7:50
# @Author   :Chang Qing
 
"""
leetcode 39

给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
示例 1： 输入：candidates = [2,3,6,7], target = 7, 所求解集为： [ [7], [2,2,3] ]

示例 2： 输入：candidates = [2,3,5], target = 8, 所求解集为： [   [2,2,2,2],   [2,3,3],   [3,5] ]

reference:  建议看解析
本题和77.组合，216.组合总和III和区别是：本题没有数量要求，可以无限重复，但是有总和的限制，所以间接的也是有个数的限制
https://cgithub.com/youngyangyang04/leetcode-master/blob/master/problems/0039.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8C.md

本题还需要startIndex来控制for循环的起始位置，对于组合问题，什么时候需要startIndex呢？

我举过例子，如果是一个集合来求组合的话，就需要startIndex，例如：77.组合，216.组合总和III。

如果是多个集合取组合，各个集合之间相互不影响，那么就不用startIndex，例如：17.电话号码的字母组合

"""


class Solution:
    def __init__(self):
        self.path = []
        self.paths = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.backtrcking(candidates, target, 0)
        return self.paths

    def backtrcking(self, candidates, target, start_index):
        if sum(self.path) > target:
            return
        if sum(self.path) == target:
            self.paths.append(self.path[:])
            return
        for i in range(start_index, len(candidates)):
            self.path.append(candidates[i])
            self.backtrcking(candidates, target, i)
            self.path.pop()

# 剪枝回溯
class Solution:
    def __init__(self):
        self.path = []
        self.paths = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        因为本题没有组合数量限制，所以只要元素总和大于target就算结束
        '''
        self.path.clear()
        self.paths.clear()

        # 为了剪枝需要提前进行排序
        candidates.sort()
        self.backtracking(candidates, target, 0, 0)
        return self.paths

    def backtracking(self, candidates: List[int], target: int, sum_: int, start_index: int) -> None:
        # Base Case
        if sum_ == target:
            self.paths.append(self.path[:]) # 因为是shallow copy，所以不能直接传入self.path
            return
        # 单层递归逻辑
        # 如果本层 sum + condidates[i] > target，就提前结束遍历，剪枝
        for i in range(start_index, len(candidates)):
            if sum_ + candidates[i] > target:
                return
            sum_ += candidates[i]
            self.path.append(candidates[i])
            self.backtracking(candidates, target, sum_, i)  # 因为无限制重复选取，所以不是i-1
            sum_ -= candidates[i]   # 回溯
            self.path.pop()        # 回溯
