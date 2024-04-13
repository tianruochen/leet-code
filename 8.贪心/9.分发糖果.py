#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :9.分发糖果.py
# @Time     :2022/3/7 上午10:47
# @Author   :Chang Qing
 
"""
leetcode 135
老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。

你需要按照以下要求，帮助老师给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
相邻的孩子中，评分高的孩子必须获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？

示例 1:

输入: [1,0,2]
输出: 5
解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。


这在leetcode上是一道困难的题目，其难点就在于贪心的策略，如果在考虑局部的时候想两边兼顾，就会顾此失彼。

那么本题我采用了两次贪心的策略：

一次是从左到右遍历，只比较右边孩子评分比左边大的情况。
一次是从右到左遍历，只比较左边孩子评分比右边大的情况。
这样从局部最优推出了全局最优，即：相邻的孩子中，评分高的孩子获得更多的糖果。
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0135.%E5%88%86%E5%8F%91%E7%B3%96%E6%9E%9C.md

"""

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candyVec = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candyVec[i] = candyVec[i - 1] + 1
        for j in range(len(ratings) - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                candyVec[j] = max(candyVec[j], candyVec[j + 1] + 1)
        return sum(candyVec)