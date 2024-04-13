#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :1.全排列.py
# @Time     :2022/3/3 下午3:09
# @Author   :Chang Qing
 

"""
leetocode 47
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

示例 1：

输入：nums = [1,1,2]
输出： [[1,1,2], [1,2,1], [2,1,1]]
示例 2：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
提示：

1 <= nums.length <= 8
-10 <= nums[i] <= 10

注意：
排列问题 不需要使用startIndex 但要用一个used数组来标记用过的数字

这道题目和46.全排列的区别在与给定一个可包含重复数字的序列，要返回所有不重复的全排列。
还要强调的是去重一定要对元素进行排序，这样我们才方便通过相邻的节点来判断是否重复使用了。
一般来说：组合问题和排列问题是在树形结构的叶子节点上收集结果，而子集问题就是取树上所有节点的结果。



这里又涉及到去重了。
reference:  建议
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0046.%E5%85%A8%E6%8E%92%E5%88%97.md
"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # res用来存放结果
        if not nums: return []
        res = []
        used = [0] * len(nums)
        def backtracking(nums, used, path):
            # 终止条件
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                # 若遇到self.path里已收录的元素，跳过
                if used[i]:
                    continue
                # 剪枝
                # used[i - 1] == true，说明同⼀树⽀nums[i - 1]使⽤过
                # used[i - 1] == false，说明同⼀树层nums[i - 1]使⽤过
                # 如果同⼀树层nums[i - 1] 使⽤过则直接跳过
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                used[i] = 1
                path.append(nums[i])
                backtracking(nums, used, path)
                path.pop()
                used[i] = 0
        # 记得给nums排序
        backtracking(sorted(nums),used,[])
        return res

# 用set去重
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        used = [False] * len(nums)

        def backtracking(nums, used, path):
            if len(path) == len(nums):
                res.append(path.copy())
                return

            deduplicate = set()
            for i, num in enumerate(nums):
                if used[i] == True:
                    continue
                if num in deduplicate:
                    continue
                used[i] = True
                path.append(nums[i])
                backtracking()
                used[i] = False
                path.pop()
                deduplicate.add(num)

        # 排列去重 不需要排序， 但集合问题（组合，子集）需要排序
        backtracking(nums,used,[])
        # backtracking(sorted(nums),used,[])

        return res



