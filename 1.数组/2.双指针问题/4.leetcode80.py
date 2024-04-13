#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :2.leetcode26.py
# @Time     :2022/2/10 下午3:10
# @Author   :Chang Qing


"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现不超过两次
思路:
快指针：遍历整个数组；
慢指针：记录可以覆写数据的位置；

题目中规定每个元素最多出现两次，因此，应检查快指针指向的元素和慢指针指针所指向单元的前一个元素是否相等。相等则不更新慢指针，只更新快指针；不相等时，先将慢指针后移一位，再将快指针指向的元素覆写入慢指针指向的单元，最后更新快指针。

边界：
当数组的长度小于等于 2 时，不需要操作，直接返回原数组即可。

初始化：
快指针用于遍历数组，但算法不可能操作序号小于 2 的元素，因此快指针初始值为 2；
初始状态下，慢指针应紧随快指针之后，因此初始值为 1；

结束条件：
快指针达到数组结尾。
reference:
https://zengdiqing.blog.csdn.net/article/details/105028587
"""


class Solution:
    def removeDoplicates(self, nums):
        slow = 1
        fast = 2
        while fast < len(nums):
            if nums[fast] == nums[slow-1]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        return nums, slow+1

    def removeDoplicates2(self, nums):
        k, length = 2, len(nums)
        while k < length:
            if nums[k] == nums[k-2]:
                length -= 1
                del nums[k]
            else:
                k += 1
        return nums, length


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4]
    res = Solution().removeDoplicates(nums)
    print(res)
    nums = [0, 0, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4]
    res = Solution().removeDoplicates2(nums)
    print(res)
