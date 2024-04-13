#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :1.组合.py
# @Time     :2022/3/2 下午5:20
# @Author   :Chang Qing
 
"""
leetcode 77
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
reference：
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0077.%E7%BB%84%E5%90%88.md
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        def backtrack(n, k, StartIndex):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(StartIndex, n + 1):
                path.append(i)
                backtrack(n, k, i+1)
                path.pop()
        backtrack(n, k, 1)
        return res

# 剪枝
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]  #存放符合条件结果的集合
        path=[]  #用来存放符合条件结果
        def backtrack(n,k,startIndex):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(startIndex,n - (k - len(path)) + 2):  #优化的地方
                path.append(i)  #处理节点
                backtrack(n,k,i+1)  #递归
                path.pop()  #回溯，撤销处理的节点
        backtrack(n,k,1)
        return res