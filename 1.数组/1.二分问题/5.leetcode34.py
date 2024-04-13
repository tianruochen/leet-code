#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :leetcode704.py
# @Time     :2022/2/9 下午4:46
# @Author   :Chang Qing


"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
解析:
    方法一: 实际就是找左右边界
    方法二: 先找到目标元素，然后向两边扩展
reference:
https://programmercarl.com/0034.%E5%9C%A8%E6%8E%92%E5%BA%8F%E6%95%B0%E7%BB%84%E4%B8%AD%E6%9F%A5%E6%89%BE%E5%85%83%E7%B4%A0%E7%9A%84%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%92%8C%E6%9C%80%E5%90%8E%E4%B8%80%E4%B8%AA%E4%BD%8D%E7%BD%AE.html
"""


class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = right - 1
            elif nums[mid] < target:
                left = left + 1
            else:
                return mid
        return -1

    def left_bound(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            print(mid)
            if target == nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
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
