#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :2.把数组排列最小的数.py
# @Time     :2022/11/8 下午5:38
# @Author   :Chang Qing


"""
题目描述
  输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

解题思路：
       * 先将整型数组转换成String数组，然后将String数组排序，最后将排好序的字符串数组拼接出来。关键就是制定排序规则。
       * 排序规则如下：
       * 若ab > ba 则 a > b，
       * 若ab < ba 则 a < b，
       * 若ab = ba 则 a = b；
       * 解释说明：
       * 比如 "3" < "31"但是 "331" > "313"，所以要将二者拼接起来进行比较
"""

from functools import cmp_to_key

class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ""
        lmb = lambda n1, n2: int(str(n1) + str(n2)) - int(str(n2) + str(n1))
        array = sorted(numbers, key=cmp_to_key(lmb))
        return ''.join([str(i) for i in array])


if __name__ == '__main__':
    a = [3, 32, 321]
    print(Solution().PrintMinNumber(a))
