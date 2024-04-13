#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :3.最长重复子数组.py
# @Time     :2022/3/24 下午7:48
# @Author   :Chang Qing
 

"""
leetcode 718

给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
示例：
输入： A: [1,2,3,2,1] B: [3,2,1,4,7] 输出：3 解释： 长度最长的公共子数组是 [3, 2, 1] 。

思路：
注意题目中说的子数组，其实就是连续子序列。这种问题动规最拿手，动规五部曲分析如下：

1.确定dp数组（dp table）以及下标的含义
dp[i][j] ：以下标i - 1为结尾的A，和以下标j - 1为结尾的B，最长重复子数组长度为dp[i][j]。

此时细心的同学应该发现，那dp[0][0]是什么含义呢？总不能是以下标-1为结尾的A数组吧。
其实dp[i][j]的定义也就决定着，我们在遍历dp[i][j]的时候i 和 j都要从1开始。

那有同学问了，我就定义dp[i][j]为 以下标i为结尾的A，和以下标j 为结尾的B，最长重复子数组长度。不行么？
行倒是行！ 但实现起来就麻烦一点，大家看下面的dp数组状态图就明白了。

2.确定递推公式
根据dp[i][j]的定义，dp[i][j]的状态只能由dp[i - 1][j - 1]推导出来。
即当A[i - 1] 和B[j - 1]相等的时候，dp[i][j] = dp[i - 1][j - 1] + 1;
根据递推公式可以看出，遍历i 和 j 要从1开始！

3.dp数组如何初始化
根据dp[i][j]的定义，dp[i][0] 和dp[0][j]其实都是没有意义的！
但dp[i][0] 和dp[0][j]要初始值，因为 为了方便递归公式dp[i][j] = dp[i - 1][j - 1] + 1;
所以dp[i][0] 和dp[0][j]初始化为0。
举个例子A[0]如果和B[0]相同的话，dp[1][1] = dp[0][0] + 1，只有dp[0][0]初始为0，正好符合递推公式逐步累加起来。

4.确定遍历顺序
外层for循环遍历A，内层for循环遍历B。
那又有同学问了，外层for循环遍历B，内层for循环遍历A。不行么？
也行，一样的，我这里就用外层for循环遍历A，内层for循环遍历B了。


https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0718.%E6%9C%80%E9%95%BF%E9%87%8D%E5%A4%8D%E5%AD%90%E6%95%B0%E7%BB%84.md
"""


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        # dp[i][j] ：以下标i - 1为结尾的A，和以下标j - 1为结尾的B，最长重复子数组长度为dp[i][j]。方便操作
        dp = [[0] * (len(B)+1) for _ in range(len(A)+1)]
        result = 0
        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                result = max(result, dp[i][j])
        return result