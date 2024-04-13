#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :4.找到字符串中所有字母异位词.py
# @Time     :2022/2/14 上午11:47
# @Author   :Chang Qing
 

"""
leetcode 438
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
说明：

字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。

"""


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        res = list()
        ls, lp = len(s), len(p)
        lo, hi = 0, lp - 1

        if lp > ls:
            return list()

        while lo + lp <= ls:
            temp = s[lo:hi + 1]
            if sorted(temp) == sorted(p):
                res.append(lo)
            lo += 1
            hi += 1

        return res

    # 高端一点带动态规划思想的比较方法，移动时不再比较整个substring，而是根据变化的局部来调整。
    def findAnagrams2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        res = list()
        ls, lp = len(s), len(p)
        if lp > ls:
            return list()

        s1 = [0 for _ in range(26)]
        s2 = [0 for _ in range(26)]

        for i in range(lp):
            s2[ord(p[i]) - 97] += 1

        for i in range(lp - 1):
            s1[ord(s[i]) - 97] += 1

        for i in range(ls - lp + 1):
            s1[ord(s[i + lp - 1]) - 97] += 1

            if s1 == s2:
                res.append(i)

            s1[ord(s[i]) - 97] -= 1

        return res

