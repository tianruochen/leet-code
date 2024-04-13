#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :3.最长公共子序列.py
# @Time     :2022/3/24 下午7:46
# @Author   :Chang Qing
 
"""
leetcode 1143

给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。
一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。
若这两个字符串没有公共子序列，则返回 0。

示例 1:
输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace"，它的长度为 3。

示例 2:
输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc"，它的长度为 3。

示例 3:
输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0。

思路：
本题和动态规划：718. 最长重复子数组区别在于这里不要求是连续的了，但要有相对顺序

1.确定dp数组（dp table）以及下标的含义
dp[i][j]：长度为[0, i - 1]的字符串text1与长度为[0, j - 1]的字符串text2的最长公共子序列为dp[i][j]
有同学会问：为什么要定义长度为[0, i - 1]的字符串text1，定义为长度为[0, i]的字符串text1不香么？
这样定义是为了后面代码实现方便，如果非要定义为为长度为[0, i]的字符串text1也可以，大家可以试一试！

2.确定递推公式
主要就是两大情况： text1[i - 1] 与 text2[j - 1]相同，text1[i - 1] 与 text2[j - 1]不相同
    如果text1[i - 1] 与 text2[j - 1]相同，那么找到了一个公共元素，所以dp[i][j] = dp[i - 1][j - 1] + 1;
    如果text1[i - 1] 与 text2[j - 1]不相同，那就看看text1[0, i - 2]与text2[0, j - 1]的最长公共子序列 和 text1[0, i - 1]与text2[0, j - 2]的最长公共子序列，取最大的。
    即：dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
    代码如下：
    if (text1[i - 1] == text2[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1] + 1;
    } else {
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
    }
3.dp数组如何初始化
先看看dp[i][0]应该是多少呢？
test1[0, i-1]和空串的最长公共子序列自然是0，所以dp[i][0] = 0;
同理dp[0][j]也是0。
其他下标都是随着递推公式逐步覆盖，初始为多少都可以，那么就统一初始为0。

4.确定遍历顺序
从递推公式，可以看出，有三个方向可以推出dp[i][j]，所以要从前向后，从上到下来遍历这个矩阵

5.举例推导dp数组
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1)+1, len(text2)+1
        """
        总结： 2个数组的子序列问题 确定dp数组（dp table）以及下标的含义 要格外注意
            为了操作方便，往往多申请一个空间。
            dp[i][j]：长度为[0, i - 1]的字符串text1与长度为[0, j - 1]的字符串text2的最长公共子序列为dp[i][j]
        """
        dp = [[0 for _ in range(len1)] for _ in range(len2)] # 先对dp数组做初始化操作
        for i in range(1, len2):
            for j in range(1, len1): # 开始列出状态转移方程
                if text1[j-1] == text2[i-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]


