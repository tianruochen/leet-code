#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :leetcode704.py
# @Time     :2022/2/9 下午4:46
# @Author   :Chang Qing


"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，
写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
reference:
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0704.%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE.md
"""


class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1

    def left_bound(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            print(mid)
            if target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        if left >= len(nums) or nums[left] != target:
            return -1
        return left

    def right_bound(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                left = mid + 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        if right < 0 or nums[right] != target:
            return -1
        return right


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 9, 9, 9, 9, 9, 9, 12]
    target = 9
    res = Solution().search(nums, target)
    print(res)
    res = Solution().left_bound(nums, target)
    print(res)
    res = Solution().right_bound(nums, target)
    print(res)
