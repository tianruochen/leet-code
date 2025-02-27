#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :4.判断子序列.py
# @Time     :2022/3/24 下午8:39
# @Author   :Chang Qing
 


"""
leetcode 392
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
示例 1： 输入：s = "abc", t = "ahbgdc" 输出：true
示例 2： 输入：s = "axc", t = "ahbgdc" 输出：false

思路：
这道题可以用双指针的思路来实现，时间复杂度就是$O(n)$）
这道题应该算是编辑距离的入门题目，因为从题意中我们也可以发现，只需要计算删除的情况，不用考虑增加和替换的情况。
所以掌握本题也是对后面要讲解的编辑距离的题目打下基础。

动态规划五部曲分析如下：

1.确定dp数组（dp table）以及下标的含义
dp[i][j] 表示以下标i-1为结尾的字符串s，和以下标j-1为结尾的字符串t，相同子序列的长度为dp[i][j]。
注意这里是判断s是否为t的子序列。即t的长度是大于等于s的。
有同学问了，为啥要表示下标i-1为结尾的字符串呢，为啥不表示下标i为结尾的字符串呢？
用i来表示也可以！
但我统一以下标i-1为结尾的字符串来计算，这样在下面的递归公式中会容易理解一些，如果还有疑惑，可以继续往下看。

2.确定递推公式
在确定递推公式的时候，首先要考虑如下两种操作，整理如下：
    if (s[i - 1] == t[j - 1]) t中找到了一个字符在s中也出现了
    if (s[i - 1] != t[j - 1]) 相当于t要删除元素，继续匹配
    if (s[i - 1] == t[j - 1])，那么dp[i][j] = dp[i - 1][j - 1] + 1;，因为找到了一个相同的字符，相同子序列长度自然要在dp[i-1][j-1]的基础上加1（如果不理解，在回看一下dp[i][j]的定义）
    if (s[i - 1] != t[j - 1])，此时相当于t要删除元素，t如果把当前元素t[j - 1]删除，那么dp[i][j] 的数值就是 看s[i - 1]与 t[j - 2]的比较结果了，即：dp[i][j] = dp[i][j - 1];

3.dp数组如何初始化
从递推公式可以看出dp[i][j]都是依赖于dp[i - 1][j - 1] 和 dp[i][j - 1]，所以dp[0][0]和dp[i][0]是一定要初始化的。
这里大家已经可以发现，在定义dp[i][j]含义的时候为什么要表示以下标i-1为结尾的字符串s，和以下标j-1为结尾的字符串t，相同子序列的长度为dp[i][j]。
dp[i][0] 表示以下标i-1为结尾的字符串，与空字符串的相同子序列长度，所以为0. dp[0][j]同理。

4.确定遍历顺序
同理从递推公式可以看出dp[i][j]都是依赖于dp[i - 1][j - 1] 和 dp[i][j - 1]，那么遍历顺序也应该是从上到下，从左到右
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # dp[i][j] 表示以下标i-1为结尾的字符串s，和以下标j-1为结尾的字符串t，相同子序列的长度为dp[i][j]。
        dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i][j-1]   # 也可以用最长公共子序列的思路  d[i][j] = max(d[i][j-1], d[i-1][j])
        if dp[-1][-1] == len(s):            # 本题是最长公共子序列的特殊情况
            return True
        return False
