#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :2.赎金信.py
# @Time     :2022/2/14 上午11:35
# @Author   :Chang Qing
 

"""
leetcode 383
给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，
判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true ；否则返回 false。
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        word = {}
        for i in magazine:
            if i in word.keys():
                word[i] += 1
            else:
                word[i] = 1
        for j in ransomNote:
            if j in word.keys():
                if word[j] != 0:
                    word[j] -= 1
                else:
                    return False
            else:
                return False
        return True


    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        import collections
        c1 = collections.Counter(ransomNote)
        c2 = collections.Counter(magazine)
        x = c1 - c2
        # x只保留值大于0的符号，当c1里面的符号个数小于c2时，不会被保留
        # 所以x只保留下了，magazine不能表达的
        if (len(x) == 0):
            return True
        else:
            return False

