#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :5.查找常用字符.py
# @Time     :2022/2/14 下午2:28
# @Author   :Chang Qing


"""
leetcode 1002
给你一个字符串数组 words ，请你找出所有在 words 的每个字符串中都出现的共用字符（ 包括重复字符），并以数组形式返回。你可以按 任意顺序 返回答案。

示例 1：

输入：words = ["bella","label","roller"] 输出：["e","l","l"] 示例 2：

输入：words = ["cool","lock","cook"] 输出：["c","o"]
"""


class Solution:
    def commonChars(self, words):
        if not words: return []
        result = []
        hash = [0] * 26  # 用来统计所有字符串里字符出现的最小频率
        for i, c in enumerate(words[0]):  # 用第一个字符串给hash初始化
            hash[ord(c) - ord('a')] += 1
        # 统计除第一个字符串外字符的出现频率
        for i in range(1, len(words)):
            hashOtherStr = [0] * 26
            for j in range(len(words[i])):
                hashOtherStr[ord(words[i][j]) - ord('a')] += 1
            # 更新hash，保证hash里统计26个字符在所有字符串里出现的最小次数
            for k in range(26):
                hash[k] = min(hash[k], hashOtherStr[k])
        # 将hash统计的字符次数，转成输出形式
        for i in range(26):
            while hash[i] != 0:  # 注意这里是while，多个重复的字符
                result.extend(chr(i + ord('a')))
                hash[i] -= 1
        return result

    def commonChars2(self, words):
        # Python 3 使用collections.Counter
        import collections
        tmp = collections.Counter(words[0])
        l = []
        for i in range(1, len(words)):
            # 使用 & 取交集
            tmp = tmp & collections.Counter(words[i])

        # 剩下的就是每个单词都出现的字符（键），个数（值）
        for j in tmp:
            v = tmp[j]
            while (v):
                l.append(j)
                v -= 1
        return l


if __name__ == '__main__':
    a = "1122"
    b = "22233"
    import collections
    # 字典不能进行与操作，但Counter可以
    a = collections.Counter(a)
    b = collections.Counter(b)
    print(a & b)
