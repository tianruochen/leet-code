#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :3.电话号码的字母组合.py
# @Time     :2022/3/2 下午7:45
# @Author   :Chang Qing

"""
leetcode 17
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

reference：
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0017.%E7%94%B5%E8%AF%9D%E5%8F%B7%E7%A0%81%E7%9A%84%E5%AD%97%E6%AF%8D%E7%BB%84%E5%90%88.md
"""
class Solution:
    def __init__(self):
        self.answer = []
        self.answers = []
        self.letter_map = {
            '0': '',
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        self.backtracking(digits, 0)
        res = []
        for an in self.answers:
            res.append("".join(an))
        return res

    def backtracking(self, digits: str, index: int) -> None:
        # 回溯函数没有返回值
        # Base Case
        if len(self.answer) == len(digits):  # 当遍历穷尽后的下一层时
            self.answers.append(self.answer[:])
            return
            # 单层递归逻辑
        letters = self.letter_map[digits[index]]
        for letter in letters:
            self.answer.append(letter)
            self.backtracking(digits, index + 1)  # 递归至下一层 + 回溯
            self.answer.pop()