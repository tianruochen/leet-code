#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :7.重复的子字符串.py
# @Time     :2022/2/14 下午9:41
# @Author   :Chang Qing

"""
leetcode 459
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。

示例 1:
输入: "abab"
输出: True
解释: 可由子字符串 "ab" 重复两次构成。

示例 2:
输入: "aba"
输出: False

示例 3:
输入: "abcabcabcabc"
输出: True
解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)

思路：
这又是一道标准的KMP的题目。

这里就要说一说next数组了，next 数组记录的就是最长相同前后缀( 字符串：KMP算法精讲 这里介绍了什么是前缀，什么是后缀，什么又是最长相同前后缀)， 如果 next[len - 1] != -1，则说明字符串有最长相同的前后缀（就是字符串里的前缀子串和后缀子串相同的最长长度）。

最长相等前后缀的长度为：next[len - 1] + 1。(这里的next数组是以统一减一的方式计算的，因此需要+1)

数组长度为：len。

如果len % (len - (next[len - 1] + 1)) == 0 ，则说明 (数组长度-最长相等前后缀的长度) 正好可以被 数组的长度整除，说明有该字符串有重复的子字符串。

数组长度减去最长相同前后缀的长度相当于是第一个周期的长度，也就是一个周期的长度，如果这个周期可以被整除，就说明整个数组就是这个周期的循环。

reference：
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0459.%E9%87%8D%E5%A4%8D%E7%9A%84%E5%AD%90%E5%AD%97%E7%AC%A6%E4%B8%B2.md
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 0:
            return False
        nxt = [0] * len(s)
        self.getNext(nxt, s)
        if nxt[-1] != 0 and len(s) % (len(s) - nxt[-1]) == 0:
            return True
        return False

    def getNext(self, nxt, s):
        nxt[0] = 0
        j = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = nxt[j - 1]
            if s[i] == s[j]:
                j += 1
            nxt[i] = j
        return nxt

# 方法二 https://www.cnblogs.com/yiluolion/p/13555541.html
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        # 子串至少重复一次
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                if all(s[j] == s[j - i] for j in range(i, n)):
                    return True

        return False


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                a = s[:i];
                j = i
                while j < n and s[j:j + i] == a:
                    j += i
                if j == n: return True

        return False

