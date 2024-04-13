#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :1.前 K 个高频元素.py
# @Time     :2022/2/15 下午4:24
# @Author   :Chang Qing
 

"""
leetcode 347
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]

思路
这道题目主要涉及到如下三块内容：

要统计元素出现频率
对频率排序
找出前K个高频元素
首先统计元素出现的频率，这一类的问题可以使用map来进行统计。

然后是对频率进行排序，这里我们可以使用一种 容器适配器就是优先级队列。

什么是优先级队列呢？

其实就是一个披着队列外衣的堆，因为优先级队列对外接口只是从队头取元素，从队尾添加元素，再无其他取元素的方式，看起来就是一个队列。
"""

# 时间复杂度：O(nlogk)
# 空间复杂度：O(n)
import heapq


class Solution:
    def topKFrequent(self, nums, k: int):
        # 要统计元素出现频率
        map_ = {}  # nums[i]:对应出现的次数
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1

        # 对频率排序
        # 定义一个小顶堆，大小为k
        pri_que = []  # 小顶堆

        # 用固定大小为k的小顶堆，扫面所有频率的数值
        for key, freq in map_.items():
            # 元组和列表也能进行比较，从左往右的顺序
            # heapq构造的是小顶堆，
            # Python自带的heapq模块实现的是最小堆，没有提供最大堆的实现。虽然有些文章通过把元素取反再放入堆，出堆时再取反，把问题转换为最小堆问题也能间接实现最大堆
            # heapq.heappush(heap, item) item 可以是元组, 函数内部会根据第一个元素 进行比较
            # heapq.heapify(list), 将一个列表转换为堆
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k:  # 如果堆的大小大于了K，则队列弹出，保证堆的大小一直为k
                heapq.heappop(pri_que)

        # 找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒序来输出到数组
        result = [0] * k
        for i in range(k - 1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        return [item[0] for item in Counter(nums).most_common(k)]
