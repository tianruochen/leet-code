#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :1.斐波那契shulie.py
# @Time     :2022/3/9 上午10:44
# @Author   :Chang Qing
 

"""
leetcode 509


动态规划
动规五部曲：

这里我们要用一个一维dp数组来保存递归的结果

确定dp数组以及下标的含义
dp[i]的定义为：第i个数的斐波那契数值是dp[i]

确定递推公式
为什么这是一道非常简单的入门题目呢？

因为题目已经把递推公式直接给我们了：状态转移方程 dp[i] = dp[i - 1] + dp[i - 2];

dp数组如何初始化
题目中把如何初始化也直接给我们了，如下：

dp[0] = 0;
dp[1] = 1;
确定遍历顺序
从递归公式dp[i] = dp[i - 1] + dp[i - 2];中可以看出，dp[i]是依赖 dp[i - 1] 和 dp[i - 2]，那么遍历的顺序一定是从前到后遍历的

举例推导dp数组
按照这个递推公式dp[i] = dp[i - 1] + dp[i - 2]，我们来推导一下，当N为10的时候，dp数组应该是如下的数列：

0 1 1 2 3 5 8 13 21 34 55

如果代码写出来，发现结果不对，就把dp数组打印出来看看和我们推导的数列是不是一致的。
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0509.%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0.md
"""


class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a, b, c = 0, 1, 0
        for i in range(1, n):
            c = a + b
            a, b = b, c
        return c

# 递归实现
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib(n - 1) + self.fib(n - 2)