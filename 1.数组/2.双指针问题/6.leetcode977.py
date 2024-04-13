#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :6.leetcode977.py
# @Time     :2022/2/10 下午5:42
# @Author   :Chang Qing
 
"""
有序数组的平方：
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
方法一：暴力破解
方法二： 双指针
reference： https://blog.csdn.net/qq_17550379/article/details/86563977

"""

class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted([i**2 for i in A])

    def sortedSquares2(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, len(A) - 1
        res = [0] * len(A)
        for k in range(len(A) - 1, -1, -1):
            if abs(A[i]) < abs(A[j]):
                res[k] = A[j] ** 2
                j -= 1
            else:
                res[k] = A[i] ** 2
                i += 1
        return res


if __name__ == '__main__':
    A = [-4, -1, 0, 3, 10]
    res = Solution().sortedSquares2(A)
    print(res)
