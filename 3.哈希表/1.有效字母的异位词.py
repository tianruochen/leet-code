#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :1.有效字母的以为此.py
# @Time     :2022/2/14 上午11:32
# @Author   :Chang Qing
 

"""
leetcode 242
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1: 输入: s = "anagram", t = "nagaram" 输出: true

示例 2: 输入: s = "rat", t = "car" 输出: false
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict

        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for x in s:
            s_dict[x] += 1

        for x in t:
            t_dict[x] += 1

        return s_dict == t_dict

if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s, t))
