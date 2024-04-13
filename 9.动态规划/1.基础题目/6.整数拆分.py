#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :6.整数拆分.py
# @Time     :2022/3/9 下午3:38
# @Author   :Chang Qing
 
"""
leetcode 343
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设 n 不小于 2 且不大于 58。

https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0343.%E6%95%B4%E6%95%B0%E6%8B%86%E5%88%86.md
"""

"""
很多人在写上面这个代码的时候会将

max(result, i*(n - i), i * self.integerBreak(n - i)) ==>
max(result, i * self.integerBreak(n - i))
写成下面的那种形式，关键问题在于没有理解函数的定义。integerBreak是将一个正整数拆分为至少两个正整数的和，也就是说i * self.integerBreak(n - i)至少是三个整数的积，那么我们在比较最大值的时候自然要将i*(n - i)给加上啦。
"""
class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        result = -1
        for i in range(1, n):
            result = max(result, i*(n - i), i * self.integerBreak(n - i))

        return result


"""
动态规划
动规五部曲，分析如下：

1.确定dp数组（dp table）以及下标的含义
dp[i]：分拆数字i为至少两个正整数的和，可以得到的最大乘积为dp[i]。

dp[i]的定义讲贯彻整个解题过程，下面哪一步想不懂了，就想想dp[i]究竟表示的是啥！

2.确定递推公式
可以想 dp[i]最大乘积是怎么得到的呢？

其实可以从1遍历j，然后有两种渠道得到dp[i].

一个是j * (i - j) 直接相乘。

一个是j * dp[i - j]，相当于是拆分(i - j)，对这个拆分不理解的话，可以回想dp数组的定义。

那有同学问了，j怎么就不拆分呢？

j是从1开始遍历，拆分j的情况，在遍历j的过程中其实都计算过了。那么从1遍历j，比较(i - j) * j和dp[i - j] * j 取最大的。递推公式：dp[i] = max(dp[i], max((i - j) * j, dp[i - j] * j));

也可以这么理解，j * (i - j) 是单纯的把整数拆分为两个数相乘，而j * dp[i - j]是拆分成两个以及两个以上的个数相乘。

如果定义dp[i - j] * dp[j] 也是默认将一个数强制拆成4份以及4份以上了。

所以递推公式：dp[i] = max({dp[i], (i - j) * j, dp[i - j] * j});

那么在取最大值的时候，为什么还要比较dp[i]呢？

因为在递推公式推导的过程中，每次计算dp[i]，取最大的而已。

3.dp的初始化
不少同学应该疑惑，dp[0] dp[1]应该初始化多少呢？

有的题解里会给出dp[0] = 1，dp[1] = 1的初始化，但解释比较牵强，主要还是因为这么初始化可以把题目过了。

严格从dp[i]的定义来说，dp[0] dp[1] 就不应该初始化，也就是没有意义的数值。

拆分0和拆分1的最大乘积是多少？

这是无解的。

这里我只初始化dp[2] = 1，从dp[i]的定义来说，拆分数字2，得到的最大乘积是1，这个没有任何异议！

4.确定遍历顺序
确定遍历顺序，先来看看递归公式：dp[i] = max(dp[i], max((i - j) * j, dp[i - j] * j));

dp[i] 是依靠 dp[i - j]的状态，所以遍历i一定是从前向后遍历，先有dp[i - j]再有dp[i]。

枚举j的时候，是从1开始的。i是从3开始，这样dp[i - j]就是dp[2]正好可以通过我们初始化的数值求出来。

所以遍历顺序为：

for (int i = 3; i <= n ; i++) {
    for (int j = 1; j < i - 1; j++) {    # i-j 要>=2 因为dp[<=1]没有意义
        dp[i] = max(dp[i], max((i - j) * j, dp[i - j] * j));
    }
}
5.举例推导dp数组
"""
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n + 1):
            # 假设对正整数 i 拆分出的第一个正整数是 j（1 <= j < i），则有以下两种方案：
            # 1) 将 i 拆分成 j 和 i−j 的和，且 i−j 不再拆分成多个正整数，此时的乘积是 j * (i-j)
            # 2) 将 i 拆分成 j 和 i−j 的和，且 i−j 继续拆分成多个正整数，此时的乘积是 j * dp[i-j]
            for j in range(1, i):
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))
        return dp[n]