#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :2.leetcode35.py
# @Time     :2022/2/9 下午4:57
# @Author   :Chang Qing

"""
求x的平方根， 只返回整数部分
解析:
方法一: 从一开始，暴力循环。一旦找到平方值等于x的数字i，直接返回i。如果找到平方值大于x的数字i，需要返回i - 1。
方法二: 二分查找。
reference:

"""


class Solution:
    def mySqrt(self, x):
        left = 0
        right = x // 2 + 1
        while (left <= right):
            mid = left + (right - left) // 2
            if mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                left = mid + 1
            else:
                return mid
        # 总结： 假设解为a, 则实际是在1-x中查找a的位置
        # 如果a不在序列中，则跳出循环时，left指向的是第一个比a大的值的位置， right指向的是比a小的最大值
        return right


if __name__ == '__main__':
    x = 20
    res = Solution().mySqrt(x)
    print(res)
