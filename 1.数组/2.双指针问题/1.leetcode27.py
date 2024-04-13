#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :1.leetcode27.py
# @Time     :2022/2/10 上午11:10
# @Author   :Chang Qing


"""
移除元素
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 $O(1)$ 额外空间并原地修改输入数组。
方法一:暴力循环，两层for， 第一层判断值，第二层移动元素
方法二:双指针
reference: https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0027.%E7%A7%BB%E9%99%A4%E5%85%83%E7%B4%A0.md
"""

class Solution:
    def removeElement(self, nums, val):
        slow = 0
        fast = 0
        """当 nums[fast] 与给定的值相等时，递增 fast 以跳过该元素。
        只要 nums[fast] != val，我们就复制 nums[fast] 到 num[slow] 并同时递增两个索引。
        重复这一过程，直到 fast 到达数组的末尾，该数组的新长度为 slow"""
        while fast < len(nums):
            if nums[fast] == val:
                fast += 1
            else:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
        return nums, slow

if __name__ == '__main__':
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    res = Solution().removeElement(nums, val)
    print(res)


