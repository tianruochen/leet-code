#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :3.py
# @Time     :2022/2/9 下午5:17
# @Author   :Chang Qing


"""寻找有序nums中第一个大于等于target的数 的位置"""
# 实际是寻找左边界的位置

class Solution:
    def search(self, nums, target):
        if nums[0] > target or nums[-1] < target:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return left


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 9, 9, 12]
    target = 9
    res = Solution().search(nums, target)
    print(res)
