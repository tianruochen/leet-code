#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :6.连续数组的最大和.py
# @Time     :2022/11/8 下午5:15
# @Author   :Chang Qing

# {6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大连续子序列的和

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if len(array) <= 0:
            return
        tempsum = 0
        maxsum = -10000
        for i in array:
            tempsum += i
            if tempsum >= maxsum:
                maxsum = tempsum
            if tempsum < 0:
                tempsum = 0
        return maxsum

