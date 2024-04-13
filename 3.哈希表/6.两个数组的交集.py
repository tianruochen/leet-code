#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :6.两个数组的交集.py
# @Time     :2022/2/14 下午3:06
# @Author   :Chang Qing
 

"""
leetcode 349
题意：给定两个数组，编写一个函数来计算它们的交集。
"""
class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))    # 两个数组先变成集合，求交集后还原为数组
