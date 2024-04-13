#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :1.leetcode209.py
# @Time     :2022/2/10 下午7:22
# @Author   :Chang Qing
 
"""
最小覆盖子串
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。

示例：
输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"

思路分析：
    窗口内是什么？
    如何移动窗口的起始位置？
    如何移动窗口的结束位置？
reference：
https://blog.csdn.net/weixin_45642918/article/details/106306452
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict

        win = defaultdict(int)
        t_dict = defaultdict(int)
        for i in t:
            t_dict[i] += 1

        # 定义指针
        left = 0
        right = 0
        # 初始化最小长度
        min_len = float('inf')

        # chr_count 用以表示滑动窗口包含字符数
        chr_count = 0
        # 最小子串起始位置
        begin = 0
        # s 长度
        s_len = len(s)
        # t 长度
        t_len = len(t)

        while right < s_len:
            # 移动窗口，
            if t_dict[s[right]] == 0:
                right += 1
                continue
            # 滑动窗口包含 T 字符数，当超过 T 其中字符个数时不在增加
            if win[s[right]] < t_dict[s[right]]:
                chr_count += 1

            win[s[right]] += 1
            right += 1

            # 当窗口包含 T 所有的字符时，缩小窗口
            while chr_count == t_len:
                # 这里更新子串的其实位置和长度
                if right - left < min_len:
                    begin = left
                    min_len = right - left
                # 缩小窗口
                if t_dict[s[left]] == 0:
                    left += 1
                    continue
                # 这里表示出窗时，窗口所包含 T 的字符刚好等于 T 中字符的个数
                # 这个时候再移动，窗口就不满足包含 T 所有字符的条件
                # 这里 chr_count - 1 ，循环结束
                if win[s[left]] == t_dict[s[left]]:
                    chr_count -= 1

                win[s[left]] -= 1
                left += 1

        return "" if min_len == float('inf') else s[begin:begin + min_len]


if __name__ == '__main__':
    S = "ADOBECODEBANC"
    T = "ABC"
    res = Solution().minWindow(S, T)
    print(res)