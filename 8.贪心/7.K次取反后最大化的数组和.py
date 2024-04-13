#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :7.K次取反后最大化的数组和.py
# @Time     :2022/3/4 下午5:55
# @Author   :Chang Qing
 

"""
leetcode 1005
给定一个整数数组 A，我们只能用以下方法修改该数组：我们选择某个索引 i 并将 A[i] 替换为 -A[i]，然后总共重复这个过程 K 次。（我们可以多次选择同一个索引 i。）

以这种方式修改数组后，返回数组可能的最大和。

示例 1：

输入：A = [4,2,3], K = 1
输出：5
解释：选择索引 (1,) ，然后 A 变为 [4,-2,3]。
示例 2：

输入：A = [3,-1,0,2], K = 3
输出：6
解释：选择索引 (1, 2, 2) ，然后 A 变为 [3,1,0,2]。
示例 3：

输入：A = [2,-3,-1,5,-4], K = 2
输出：13
解释：选择索引 (1, 4) ，然后 A 变为 [2,3,-1,5,4]。
提示：

1 <= A.length <= 10000
1 <= K <= 10000
-100 <= A[i] <= 100


https://github.com/youngyangyang04/leetcode-master/blob/master/problems/1005.K%E6%AC%A1%E5%8F%96%E5%8F%8D%E5%90%8E%E6%9C%80%E5%A4%A7%E5%8C%96%E7%9A%84%E6%95%B0%E7%BB%84%E5%92%8C.md
"""

class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A = sorted(A, key=abs, reverse=True) # 将A按绝对值从大到小排列
        for i in range(len(A)):
            if K > 0 and A[i] < 0:
                A[i] *= -1
                K -= 1
        if K > 0:
            A[-1] *= (-1)**K #取A最后一个数只需要写-1
        return sum(A)
