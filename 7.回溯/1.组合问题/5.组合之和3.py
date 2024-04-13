#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :5.组合之和3.py
# @Time     :2022/3/2 下午8:24
# @Author   :Chang Qing
 
"""
leetcode 40
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明： 所有数字（包括目标数）都是正整数。 解集不能包含重复的组合。

示例 1: 输入: candidates = [10,1,2,7,6,1,5], target = 8, 所求解集为: [ [1, 7], [1, 2, 5], [2, 6], [1, 1, 6] ]

示例 2: 输入: candidates = [2,5,2,1,2], target = 5, 所求解集为: [   [1,2,2],   [5] ]

强烈建议看解析：
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0040.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CII.md
"""

#回溯+巧妙去重(省去使用used

class Solution:
    def __init__(self):
        self.path = []
        self.paths = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        必须要排序
        [10,1,2,7,6,1,5]
        8
        如果不排序，结果是：[[1,2,5],[1,7],[1,6,1],[2,6],[2,1,5],[7,1]]
        实际答案是： [[1,1,6],[1,2,5],[1,7],[2,6]]
        """
        candidates.sort()        # 必须要先排序
        self.tracebacking(candidates, target, 0)
        return self.paths

    def tracebacking(self, candidates, target, start_index):
        if sum(self.path) == target:
            self.paths.append(self.path[:])
            return
        if sum(self.path) > target:       # 注意剪枝
            return
        used = set()
        for i in range(start_index, len(candidates)):
            if candidates[i] in used:
                continue
            used.add(candidates[i])
            self.path.append(candidates[i])
            self.tracebacking(candidates, target, i + 1)
            self.path.pop()


class Solution:
    def __init__(self):
        self.paths = []
        self.path = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        类似于求三数之和，求四数之和，为了避免重复组合，需要提前进行数组排序
        '''
        self.paths.clear()
        self.path.clear()
        # 必须提前进行数组排序，避免重复
        candidates.sort()
        self.backtracking(candidates, target, 0, 0)
        return self.paths

    def backtracking(self, candidates: List[int], target: int, sum_: int, start_index: int) -> None:
        # Base Case
        if sum_ == target:
            self.paths.append(self.path[:])
            return

        # 单层递归逻辑
        for i in range(start_index, len(candidates)):
            # 剪枝，同39.组合总和
            if sum_ + candidates[i] > target:
                return

            # 跳过同一树层使用过的元素
            if i > start_index and candidates[i] == candidates[i - 1]:
                continue

            sum_ += candidates[i]
            self.path.append(candidates[i])
            self.backtracking(candidates, target, sum_, i + 1)   # 这里是i+1，每个数字在每个组合中只能使用一次
            self.path.pop()  # 回溯，为了下一轮for loop
            sum_ -= candidates[i]  # 回溯，为了下一轮for loop

# 回溯+去重（使用used）
class Solution:
    def __init__(self):
        self.paths = []
        self.path = []
        self.used = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        类似于求三数之和，求四数之和，为了避免重复组合，需要提前进行数组排序
        本题需要使用used，用来标记区别同一树层的元素使用重复情况：注意区分递归纵向遍历遇到的重复元素，和for循环遇到的重复元素，这两者的区别
        '''
        self.paths.clear()
        self.path.clear()
        self.usage_list = [False] * len(candidates)
        # 必须提前进行数组排序，避免重复
        candidates.sort()
        self.backtracking(candidates, target, 0, 0)
        return self.paths

    def backtracking(self, candidates: List[int], target: int, sum_: int, start_index: int) -> None:
        # Base Case
        if sum_ == target:
            self.paths.append(self.path[:])
            return

        # 单层递归逻辑
        for i in range(start_index, len(candidates)):
            # 剪枝，同39.组合总和
            if sum_ + candidates[i] > target:
                return

            # 检查同一树层是否出现曾经使用过的相同元素
            # 若数组中前后元素值相同，但前者却未被使用(used == False)，说明是for loop中的同一树层的相同元素情况
            if i > 0 and candidates[i] == candidates[i - 1] and self.usage_list[i - 1] == False:
                continue

            sum_ += candidates[i]
            self.path.append(candidates[i])
            self.usage_list[i] = True
            self.backtracking(candidates, target, sum_, i + 1)
            self.usage_list[i] = False  # 回溯，为了下一轮for loop
            self.path.pop()  # 回溯，为了下一轮for loop
            sum_ -= candidates[i]  # 回溯，为了下一轮for loop


# 用set去重
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()

        def backtracking(start, path):
            if sum(path) == target:
                res.append(path)
            elif sum(path) < target:
                used = set()
                for i in range(start, len(candidates)):
                    if candidates[i] in used:
                        continue
                    else:
                        used.add(candidates[i])
                        backtracking(i + 1, path + [candidates[i]])

        backtracking(0, [])

        return res
