#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :6.KMP算法.py
# @Time     :2022/2/14 下午7:41
# @Author   :Chang Qing

"""
示例 1: 输入: haystack = "hello", needle = "ll" 输出: 2

示例 2: 输入: haystack = "aaaaa", needle = "bba" 输出: -1

说明: 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。


"""

#
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         a = len(needle)
#         b = len(haystack)
#         if a == 0:
#             return 0
#         next = self.getnext(a, needle)
#         p = -1
#         for j in range(b):
#             while p >= 0 and needle[p + 1] != haystack[j]:
#                 p = next[p]
#             if needle[p + 1] == haystack[j]:
#                 p += 1
#             if p == a - 1:
#                 return j - a + 1
#         return -1
#
#     def getnext(self, a, needle):
#         next = ['' for i in range(a)]
#         k = -1
#         next[0] = k
#         for i in range(1, len(needle)):
#             while (k > -1 and needle[k + 1] != needle[i]):
#                 k = next[k]
#             if needle[k + 1] == needle[i]:
#                 k += 1
#             next[i] = k
#         return next


# // 方法二
def KMP_algorithm(string, substring):
    '''
    KMP字符串匹配的主函数
    若存在字串返回字串在字符串中开始的位置下标，或者返回-1
    '''
    pnext = gen_pnext(substring)
    n = len(string)
    m = len(substring)
    i, j = 0, 0
    while (i < n) and (j < m):
        if (string[i] == substring[j]):
            i += 1
            j += 1
        elif (j != 0):
            j = pnext[j - 1]
        else:
            i += 1
    if (j == m):
        return i - j
    else:
        return -1


def gen_pnext(substring):
    """
    构造临时数组pnext
    """
    index, m = 0, len(substring)   # 从第二个元素开始！ index指向前缀末尾 所以初始化为0
    pnext = [0] * m
    i = 1                          # 从第二个元素开始！ i指向后缀末尾 所以初始化为1
    while i < m:
        if (substring[i] == substring[index]):
            pnext[i] = index + 1
            index += 1
            i += 1
        elif (index != 0):
            index = pnext[index - 1]
        else:
            pnext[i] = 0
            i += 1
    return pnext

def getNext(nxt, s):     # 与gen_pnext 效果一样   卡尔视频更好理解
    nxt[0] = 0
    j = 0
    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]:
            j = nxt[j - 1]
        if s[i] == s[j]:
            j += 1
        nxt[i] = j
    return nxt


if __name__ == "__main__":
    string = 'abcxabcdabcdabcy'
    substring = 'abcdabcy'
    out = KMP_algorithm(string, substring)
    print(out)
