#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :7.leetcode15.py
# @Time     :2022/2/14 下午3:31
# @Author   :Chang Qing
 
"""
leetcode 15
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
注意： 答案中不可以包含重复的三元组。

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为： [ [-1, 0, 1], [-1, -1, 2] ]


思路：
拿这个nums数组来举例，首先将数组排序，然后有一层for循环，i从下标0的地方开始，同时定一个下标left 定义在i+1的位置上，定义下标right 在数组结尾的位置上。

依然还是在数组中找到 abc 使得a + b +c =0，我们这里相当于 a = nums[i] b = nums[left] c = nums[right]。

接下来如何移动left 和right呢， 如果nums[i] + nums[left] + nums[right] > 0 就说明 此时三数之和大了，因为数组是排序后了，所以right下标就应该向左移动，这样才能让三数之和小一些。

如果 nums[i] + nums[left] + nums[right] < 0 说明 此时 三数之和小了，left 就向右移动，才能让三数之和大一些，直到left与right相遇为止。

reference：
https://programmercarl.com/0015.%E4%B8%89%E6%95%B0%E4%B9%8B%E5%92%8C.html#%E5%8F%8C%E6%8C%87%E9%92%88

"""


class Solution:
    def threeSum(self, nums):
        ans = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            left = i + 1
            right = n - 1
            if nums[i] > 0:
                break
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left != right and nums[left] == nums[left + 1]: left += 1
                    while left != right and nums[right] == nums[right - 1]: right -= 1
                    left += 1
                    right -= 1
        return ans

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
                val = target - (nums[i] + nums[j])
                if val in hashmap:
                    # make sure no duplicates.
                    count = (nums[i] == val) + (nums[j] == val)
                    if hashmap[val] > count:
                        ans.add(tuple(sorted([nums[i], nums[j], val])))
        return ans