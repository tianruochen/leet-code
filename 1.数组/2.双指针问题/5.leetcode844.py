#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :5.leetcode844.py
# @Time     :2022/2/10 下午5:37
# @Author   :Chang Qing
 

"""
比较含退格的字符串: 给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。
思路：
方法1： 使用栈
方法2：使用双指针
reference： https://www.cnblogs.com/xugenpeng/p/10035916.html
"""


class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def build(s):
            stack = []
            for c in s:
                if c != '#':
                    stack.append(c)
                elif stack:
                    stack.pop()
            return ''.join(stack)
        return build(S) == build(T)

    def backspaceCompare2(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        # skip 统计回退符号的个数
        i, j, s_skip, t_skip = len(S) - 1, len(T) - 1, 0, 0
        while i >= 0 or j >= 0:
            # 找到字符串S所对应结果的下一个字符
            while i >= 0:
                if S[i] == '#':
                    i -= 1
                    s_skip += 1
                elif s_skip > 0:
                    i -= 1
                    s_skip -= 1
                else:
                    break

            # 找到字符串T所对应结果的下一个字符
            while j >= 0:
                if T[j] == '#':
                    j -= 1
                    t_skip += 1
                elif t_skip > 0:
                    j -= 1
                    t_skip -= 1
                else:
                    break

            # 如果索引i和j所对应的字符不相等，返回False
            if i >= 0 and j >= 0 and S[i] != T[j]:
                return False

            # 如果遍历完一个字符的同时，另一个字符还未遍历完，返回False
            if (i >= 0) != (j >= 0):
                return False

        return True


if __name__ == '__main__':
    S = "ab#c"
    T = "ad#c"
    res = Solution().backspaceCompare(S, T)
    print(res)