#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :11.四数之和2.py
# @Time     :2022/2/14 下午4:16
# @Author   :Chang Qing
 
"""
leetcode 454
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。
为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -2^28 到 2^28 - 1 之间，最终结果不会超过 2^31 - 1 。
例如:

输入: A = [ 1, 2] B = [-2,-1] C = [-1, 2] D = [ 0, 2] 输出: 2 解释: 两个元组如下:

(0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
(1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

思路：
本题解题步骤：

首先定义 一个dict放a和b两数之和，value 放a和b两数之和出现的次数。
遍历大A和大B数组，统计两个数组元素之和，和出现的次数，放到map中。
定义int变量count，用来统计 a+b+c+d = 0 出现的次数。
在遍历大C和大D数组，找到如果 0-(c+d) 在map中出现过的话，就用count把map中key对应的value也就是出现次数统计出来。
最后返回统计值 count 就可以了
"""


class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        # use a dict to store the elements in nums1 and nums2 and their sum
        hashmap = dict()
        for n1 in nums1:
            for n2 in nums2:
                if n1 + n2 in hashmap:
                    hashmap[n1 + n2] += 1
                else:
                    hashmap[n1 + n2] = 1

        # if the -(a+b) exists in nums3 and nums4, we shall add the count
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                key = - n3 - n4
                if key in hashmap:
                    count += hashmap[key]
        return count


