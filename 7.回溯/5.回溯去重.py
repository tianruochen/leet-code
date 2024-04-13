#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :5.回溯去重.py
# @Time     :2022/3/3 下午3:42
# @Author   :Chang Qing
 


"""
对于子集问题，也可以用set第同一层节点去重，但一定要现排序。
而递增子序列问题没有（不能）先对集合排序（破坏了题意），却还可以用set去重是因为它有额外的限制（递增）。
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95%E5%8E%BB%E9%87%8D%E9%97%AE%E9%A2%98%E7%9A%84%E5%8F%A6%E4%B8%80%E7%A7%8D%E5%86%99%E6%B3%95.md
"""