#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :8.字符串的全排列.py
# @Time     :2022/11/8 下午4:40
# @Author   :Chang Qing
 

"""
题目描述：
  输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

解题思路：
  1.使用迭代的方法，求出所有排列，然后过滤并排序。
      思路：递归法，问题转换为先固定第一个字符，求剩余字符的排列；求剩余字符排列时跟原问题一样。
        (1) 遍历出所有可能出现在第一个位置的字符（即：依次将第一个字符同后面所有字符交换）；
        (2) 固定第一个字符，求后面字符的排列（即：在第1步的遍历过程中，插入递归进行实现）。
  1.直接用itertools中现成的函数permutations返回所有的排列，然后过滤并排序。
"""

class Solution:
    def permutation(self, s: str) -> List[str]:
        if len(s) <= 1:
            return [s]
        else:
            temp_list = []
            for i in range(len(s)):  # 遍历字符串 s 中的每个字符
                for j in self.permutation(s[0:i] + s[i+1:]):  # 把除了s[i]字符以外的字符组成字符串然后让它迭代
                    temp_list.append(s[i]+j)
            return list(set(temp_list))

def permutation(s):
    if len(s) <= 1:
        return [s]
    else:
        temp_list = []
        for i in range(len(s)):  # 遍历字符串 s 中的每个字符
            for j in permutation(s[0:i] + s[i+1:]):  # 把除了s[i]字符以外的字符组成字符串然后让它迭代
                 temp_list.append(s[i]+j)
        return temp_list

def Permutation(self, ss):
    # write code here
    if len(ss) <= 0:
        return []
    res = list()
    self.perm(ss, res, '')
    uniq = list(set(res))
    return sorted(uniq)


def perm(self, ss, res, path):
    if ss == '':
        res.append(path)
    else:
        for i in range(len(ss)):
            self.perm(ss[:i] + ss[i + 1:], res, path + ss[i])


# 方法二
def string_permutations(s, i, n):
    if i == n:
        print(''.join(s))
    else:
        for j in range(i, n):               # 每次只交换一个元素, 然后排列剩余元素
            s[i], s[j] = s[j], s[i]
            string_permutations(s, i + 1, n)
            s[i], s[j] = s[j], s[i]


a = "day"
x = len(a)
s = list(a)
print(string_permutations(s, 0, x))

# 方法三
import itertools


class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        return sorted(list(set(map(''.join, itertools.permutations(ss)))))


# itertools.permutations: 返回可迭代对象的所有排列，返回一个迭代器