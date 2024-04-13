#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :15.合并区间.py
# @Time     :2022/3/7 下午3:17
# @Author   :Chang Qing
 

"""
leetcode 56
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: intervals = [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
注意：输入类型已于2019年4月15日更改。 请重置默认代码定义以获取新方法签名。
提示：

intervals[i][0] <= intervals[i][1]

思路：
大家应该都感觉到了，此题一定要排序，那么按照左边界排序，还是右边界排序呢？

都可以！

那么我按照左边界排序，排序之后局部最优：每次合并都取最大的右边界，这样就可以合并更多的区间了，整体最优：合并所有重叠的区间。

局部最优可以推出全局最优，找不出反例，试试贪心。

那有同学问了，本来不就应该合并最大右边界么，这和贪心有啥关系？

有时候贪心就是常识！哈哈

按照左边界从小到大排序之后，如果 intervals[i][0] < intervals[i - 1][1] 即intervals[i]左边界 < intervals[i - 1]右边界，则一定有重复，因为intervals[i]的左边界一定是大于等于intervals[i - 1]的左边界。

即：intervals[i]的左边界在intervals[i - 1]左边界和右边界的范围内，那么一定有重复！

https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0056.%E5%90%88%E5%B9%B6%E5%8C%BA%E9%97%B4.md
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0: return intervals
        intervals.sort(key=lambda x: x[0])
        result = []
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            last = result[-1]
            if last[1] >= intervals[i][0]:
                result[-1] = [last[0], max(last[1], intervals[i][1])]
            else:
                result.append(intervals[i])
        return result