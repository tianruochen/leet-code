#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :2.组合之和3.py
# @Time     :2022/3/2 下午5:26
# @Author   :Chang Qing
 

"""
leetcode 216
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。
示例 1: 输入: k = 3, n = 7 输出: [[1,2,4]]

示例 2: 输入: k = 3, n = 9 输出: [[1,2,6], [1,3,5], [2,3,4]]
思路：
相对于77. 组合，无非就是多了一个限制，本题是要找到和为n的k个数的组合，而整个集合已经是固定的了[1,...,9]。
reference：
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0216.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CIII.md
"""


class Solution:
    def __init__(self):
        self.path = []
        self.paths = []

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.tracebacking(n, k, 1)
        return self.paths

    def tracebacking(self, n, k, start_index):
        if sum(self.path) == n and len(self.path) == k:
            self.paths.append(self.path[:])
            return
        for i in range(start_index, 10):
            self.path.append(i)
            self.tracebacking(n, k, i + 1)
            self.path.pop()