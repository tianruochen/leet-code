#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :2.leetcode26.py
# @Time     :2022/2/10 下午3:10
# @Author   :Chang Qing
 

"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
思路：双指针
数组完成排序后，我们可以放置两个指针 slow 和 fast，其中 slow 是慢指针，而 fast 是快指针。只要 nums[slow]==nums[fast]，我们就增加 fast 以跳过重复项。

当我们遇到 nums[slow]!=nums[fast] 时，跳过重复项的运行已经结束，因此我们必须把 nums[fast]的值复制到 nums[slow+1] 。然后递增 slow，接着我们将再次重复相同的过程，直到 fast 到达数组的末尾为止。


"""

class Solution:
    def removeDoplicates(self, nums):
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return nums, slow+1      #(返回的是剩余元素的数量，而不是下标，所以要+1)

if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    res = Solution().removeDoplicates(nums)
    print(res)

