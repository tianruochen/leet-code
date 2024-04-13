#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :7.快乐数.py
# @Time     :2022/2/14 下午3:08
# @Author   :Chang Qing
 

"""
leetcode 202
编写一个算法来判断一个数 n 是不是快乐数。
「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，
也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。
如果 n 是快乐数就返回 True ；不是，则返回 False 。

思路：
这道题目看上去貌似一道数学问题，其实并不是！
题目中说了会 无限循环，那么也就是说求和的过程中，sum会重复出现，这对解题很重要！
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0202.%E5%BF%AB%E4%B9%90%E6%95%B0.md
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        def calculate_happy(num):
            sum_ = 0

            # 从个位开始依次取，平方求和
            while num:
                sum_ += (num % 10) ** 2
                num = num // 10
            return sum_

        # 记录中间结果
        record = set()

        while True:
            n = calculate_happy(n)
            if n == 1:
                return True

            # 如果中间结果重复出现，说明陷入死循环了，该数不是快乐数
            if n in record:
                return False
            else:
                record.add(n)
