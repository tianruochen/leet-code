#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :5.左旋转字符串.py
# @Time     :2022/2/14 下午7:37
# @Author   :Chang Qing
 


"""
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。
比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

示例 1：
输入: s = "abcdefg", k = 2
输出: "cdefgab"

示例 2：
输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"

思路：
反转区间为前n的子串
反转区间为n到末尾的子串
反转整个字符串
"""

# 方法一：可以使用切片方法
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[0:n]


    # 方法三：如果连reversed也不让使用，那么自己手写一个
    def reverseLeftWords2(self, s: str, n: int) -> str:
        def reverse_sub(lst, left, right):
            while left < right:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1

        res = list(s)
        end = len(res) - 1
        reverse_sub(res, 0, n - 1)
        reverse_sub(res, n, end)
        reverse_sub(res, 0, end)
        return ''.join(res)
