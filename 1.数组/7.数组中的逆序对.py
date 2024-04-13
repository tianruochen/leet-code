#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :7.数组中的你是真.py
# @Time     :2022/11/8 下午7:25
# @Author   :Chang Qing
 
"""
题目描述
  在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。
并将P对1000000007取模的结果输出。 即输出P%1000000007
"""


class Solution:
    def InversePairs(self, data):
        # write code here
        l = len(data)
        count = 0
        for i in range(l - 1):
            for j in range(i+1, l):
                if data[i] > data[j]:
                    count += 1
        return count

# 最后网上还看到一个更加简洁（牛逼）的方法：
# 先将原序列排序，然后从排完序的数组中取出最小的，它在原数组中的位置表示有多少比它大的数在它前面，每取出一个在原数组中删除该元素，保证后面取出的元素在原数组中是最小的，这样其位置才能表示有多少比它大的数在它前面，即逆序对数。
class Solution:
    def InversePairs(self, data):
        count = 0
        copy = []
        for i in data:
            copy.append(i)
        copy.sort()
        for i in range(len(copy)):
            count += data.index(copy[i])
            data.remove(copy[i])
        return count%1000000007
a=[1,2,3,4,5,6,7,0]
Solution().InversePairs(a)