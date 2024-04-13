#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :7.leetcode15.py
# @Time     :2022/2/14 下午3:31
# @Author   :Chang Qing
 
"""
leetcode 18

题意：给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

思路：
四数之和，和15.三数之和是一个思路，都是使用双指针法, 基本解法就是在15.三数之和 的基础上再套一层for循环。

但是有一些细节需要注意，例如： 不要判断nums[k] > target 就返回了，三数之和 可以通过 nums[i] > 0 就返回了，因为 0 已经是确定的数了，四数之和这道题目 target是任意值。（大家亲自写代码就能感受出来）

15.三数之和的双指针解法是一层for循环num[i]为确定值，然后循环内有left和right下标作为双指针，找到nums[i] + nums[left] + nums[right] == 0。

四数之和的双指针解法是两层for循环nums[k] + nums[i]为确定值，依然是循环内有left和right下标作为双指针，找出nums[k] + nums[i] + nums[left] + nums[right] == target的情况，三数之和的时间复杂度是$O(n^2)$，四数之和的时间复杂度是$O(n^3)$ 。

那么一样的道理，五数之和、六数之和等等都采用这种解法。
reference：
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0018.%E5%9B%9B%E6%95%B0%E4%B9%8B%E5%92%8C.md
"""


# 双指针法
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]: continue
            for k in range(i + 1, n):
                if k > i + 1 and nums[k] == nums[k - 1]: continue
                p = k + 1
                q = n - 1

                while p < q:
                    if nums[i] + nums[k] + nums[p] + nums[q] > target:
                        q -= 1
                    elif nums[i] + nums[k] + nums[p] + nums[q] < target:
                        p += 1
                    else:
                        res.append([nums[i], nums[k], nums[p], nums[q]])
                        while p < q and nums[p] == nums[p + 1]: p += 1
                        while p < q and nums[q] == nums[q - 1]: q -= 1
                        p += 1
                        q -= 1
        return res


    # 哈希表法
    def fourSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # use a dict to store value:showtimes
        hashmap = dict()
        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1

        # good thing about using python is you can use set to drop duplicates.
        ans = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    val = target - (nums[i] + nums[j] + nums[k])
                    if val in hashmap:
                        # make sure no duplicates.
                        count = (nums[i] == val) + (nums[j] == val) + (nums[k] == val)
                        if hashmap[val] > count:
                            ans.add(tuple(sorted([nums[i], nums[j], nums[k], val])))
                    else:
                        continue
        return ans
