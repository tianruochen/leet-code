#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :3.py
# @Time     :2022/2/9 下午5:17
# @Author   :Chang Qing


"""寻找有序nums中第一个大于target的数 的位置"""
# 实际是寻找右边界的位置 等于target的最后一个位置

class Solution:
    def search(self, nums, target):
        if nums[0] > target or nums[-1] < target:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            print(mid)
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        # 如果是返回右边界 则return right+1   right=left-1
        return right + 1

if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    res = Solution().search(nums, target)
    print(res)
