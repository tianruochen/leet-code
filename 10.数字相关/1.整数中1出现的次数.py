#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :1整数中1出现的次数.py
# @Time     :2022/11/8 下午5:26
# @Author   :Chang Qing

"""
题目描述
  求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,
但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。

解题思路：
  以百位为例：
    百位数为0，情况由更高位决定，10022，百位数字出现1的情况:100-199，1100-1199，2100-2199，...9100-9199，共100*10=1000种。即高位(10) * 位置(100)
    百位数为1，情况由更高位和低位数决定，10122，百位数字出现1的情况为:100-199, 1100-1199, 2100-2199,...9100-9199,10100-10122，共1000+23种。即高位(10) * 位置(100) + 低位(23)
    百位数大于1，10222，百位数出现1的情况为: 100-199, 1100-1199, ...9100-9199, 10100-10199 共1100种。即(高位(10)+1) * 位置(100)
"""
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        res = 0
        i = 1  # 个位开始
        while n // i != 0:
            high = n // (i * 10)  # 高位数
            current = (n // i) % 10  # 第i位数
            low = n - (n // i) * i  # 低位数
            if current == 0:
                res += high * i
            elif current == 1:
                res += high * i + low + 1
            else:
                res += (high + 1) * i
            i *= 10
        return res

