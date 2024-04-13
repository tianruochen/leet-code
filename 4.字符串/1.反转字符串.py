#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :1.反转字符串.py
# @Time     :2022/2/14 下午5:31
# @Author   :Chang Qing

"""
leetcode 344
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 $O(1)$ 的额外空间解决这一问题。
"""

class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1

        # 该方法已经不需要判断奇偶数，经测试后时间空间复杂度比用 for i in range(right//2)更低
        # 推荐该写法，更加通俗易懂
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
