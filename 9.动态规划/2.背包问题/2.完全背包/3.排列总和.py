#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :3.排列总和.py
# @Time     :2022/3/24 上午11:59
# @Author   :Chang Qing
 

"""
leetcode 377
给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。

示例:

nums = [1, 2, 3] target = 4

所有可能的组合为： (1, 1, 1, 1) (1, 1, 2) (1, 2, 1) (1, 3) (2, 1, 1) (2, 2) (3, 1)

请注意，顺序不同的序列被视作不同的组合。

因此输出为 7。

思路：
本题题目描述说是求组合，但又说是可以元素相同顺序不同的组合算两个组合，其实就是求排列！（先背包再物品）
求装满背包有几种方法，递归公式都是一样的，没有什么差别，但关键在于遍历顺序！



"""

class Solution:
    def combinationSum4(self, nums, target):
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target+1):
            for j in nums:
                if i >= j:
                    dp[i] += dp[i - j]
        return dp[-1]

if __name__ == '__main__':
    nums = [1, 2, 3]
    target = 4
    print(Solution().combinationSum4(nums, target))