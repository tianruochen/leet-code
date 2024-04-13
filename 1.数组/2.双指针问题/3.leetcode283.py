#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :2.leetcode26.py
# @Time     :2022/2/10 下午3:10
# @Author   :Chang Qing





class Solution:
    def moveZero(self, nums):
        """
        给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序
        """
        slow, fast = 0, 0
        while fast <= len(nums) - 1:
            if nums[fast] != 0:              # 常规的双指针解题模板，得到包含所有非零元素的新数组
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        for i in range(slow, fast):          # 将剩余部分全部变为0
            nums[i] = 0


    def moveValue(self, nums, val):
        """
        给定一个数组 nums，移除val, 同时保持非零元素的相对顺序
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                if fast != slow:       # 这个判断不能少
                    nums[fast] = val
                slow += 1
        return nums



if __name__ == '__main__':
    nums = [1, 0, 1, 0, 3, 12]
    res = Solution().moveZero(nums)
    print(res)
    res = Solution().moveValue(nums, 3)
    print(res)
