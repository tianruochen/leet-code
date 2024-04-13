#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :1.回文子串.py
# @Time     :2022/3/24 下午9:28
# @Author   :Chang Qing
 

"""
leetcode 647

给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

示例 1：
输入："abc" 输出：3 解释：三个回文子串: "a", "b", "c"
示例 2：
输入："aaa" 输出：6 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"

思路：
动规五部曲：

1.确定dp数组（dp table）以及下标的含义
  布尔类型的dp[i][j]：表示区间范围[i,j] （注意是左闭右闭）的子串是否是回文子串，如果是dp[i][j]为true，否则为false。

2.确定递推公式
    在确定递推公式时，就要分析如下几种情况。
    整体上是两种，就是s[i]与s[j]相等，s[i]与s[j]不相等这两种。

    当s[i]与s[j]不相等，那没啥好说的了，dp[i][j]一定是false。

当s[i]与s[j]相等时，这就复杂一些了，有如下三种情况
    情况一：下标i 与 j相同，同一个字符例如a，当然是回文子串
    情况二：下标i 与 j相差为1，例如aa，也是文子串
    情况三：下标：i 与 j相差大于1的时候，例如cabac，此时s[i]与s[j]已经相同了，我们看i到j区间是不是回文子串就看aba是不是回文就可以了，那么aba的区间就是 i+1 与 j-1区间，这个区间是不是回文就看dp[i + 1][j - 1]是否为true。

3.dp数组如何初始化
    dp[i][j]可以初始化为true么？ 当然不行，怎能刚开始就全都匹配上了。
    所以dp[i][j]初始化为false。

4.确定遍历顺序
    遍历顺序可有有点讲究了。
    首先从递推公式中可以看出，情况三是根据dp[i + 1][j - 1]是否为true，在对dp[i][j]进行赋值true的。
    所以一定要从下到上，从左到右遍历，这样保证dp[i + 1][j - 1]都是经过计算的。
5.举例推导dp数组

"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        #   布尔类型的dp[i][j]：表示区间范围[i,j] （注意是左闭右闭）的子串是否是回文子串，如果是dp[i][j]为true，否则为false。
        dp = [[False] * len(s) for _ in range(len(s))]
        result = 0
        for i in range(len(s)-1, -1, -1): #注意遍历顺序
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1: #情况一 和 情况二
                        result += 1
                        dp[i][j] = True
                    elif dp[i+1][j-1]: #情况三
                        result += 1
                        dp[i][j] = True
        return result

# 双指针法
class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            result += self.extend(s, i, i, len(s))  # 以i为中心
            result += self.extend(s, i, i + 1, len(s))  # 以i和i+1为中心
        return result

    def extend(self, s, i, j, n):
        res = 0
        while i >= 0 and j < n and s[i] == s[j]:
            i -= 1
            j += 1
            res += 1
        return res