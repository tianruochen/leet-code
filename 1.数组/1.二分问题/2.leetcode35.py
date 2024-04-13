#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :2.leetcode35.py
# @Time     :2022/2/9 下午4:57
# @Author   :Chang Qing

"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
reference:
https://programmercarl.com/0035.%E6%90%9C%E7%B4%A2%E6%8F%92%E5%85%A5%E4%BD%8D%E7%BD%AE.html
"""


class Solution:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while (left <= right):
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        # 如果nums中所有的数都比target小， 循环结束 left=len(nums)
        # 如果nums中所有的数都比target大， 循环结束 left = 0
        # 如果target 介于nums最大与最小值之间， 循环结束 left指向第一个大于target的位置
        # 总之: 将target放入left指向的位置，整个序列仍旧有序
        return left


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 5
    res = Solution().searchInsert(nums, target)
    print(res)
