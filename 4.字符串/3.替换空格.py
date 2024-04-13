#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :3.替换空格.py
# @Time     :2022/2/14 下午5:37
# @Author   :Chang Qing

"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1： 输入：s = "We are happy."
输出："We%20are%20happy."
"""
class Solution:
    def replaceSpace(self, s: str) -> str:
        counter = s.count(' ')

        res = list(s)
        # 每碰到一个空格就多拓展两个格子，1 + 2 = 3个位置存’%20‘
        res.extend([' '] * counter * 2)

        # 原始字符串的末尾，拓展后的末尾
        left, right = len(s) - 1, len(res) - 1

        while left >= 0:
            if res[left] != ' ':
                res[right] = res[left]
                right -= 1
            else:
                # [right - 2, right), 左闭右开
                res[right - 2: right + 1] = '%20'
                right -= 3
            left -= 1
        return ''.join(res)

