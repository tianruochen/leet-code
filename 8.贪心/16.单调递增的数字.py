#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :16.单调递增的数字.py
# @Time     :2022/3/7 下午4:35
# @Author   :Chang Qing
 

"""
leetcode 738
给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。

（当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）

示例 1:

输入: N = 10
输出: 9
示例 2:

输入: N = 1234
输出: 1234
示例 3:

输入: N = 332
输出: 299
说明: N 是在 [0, 10^9] 范围内的一个整数。

思路：
题目要求小于等于N的最大单调递增的整数，那么拿一个两位的数字来举例。

例如：98，一旦出现strNum[i - 1] > strNum[i]的情况（非单调递增），首先想让strNum[i - 1]--，然后strNum[i]给为9，这样这个整数就是89，即小于98的最大的单调递增整数。

这一点如果想清楚了，这道题就好办了。

局部最优：遇到strNum[i - 1] > strNum[i]的情况，让strNum[i - 1]--，然后strNum[i]给为9，可以保证这两位变成最大单调递增整数。

全局最优：得到小于等于N的最大单调递增的整数。

但这里局部最优推出全局最优，还需要其他条件，即遍历顺序，和标记从哪一位开始统一改成9。

此时是从前向后遍历还是从后向前遍历呢？

从前向后遍历的话，遇到strNum[i - 1] > strNum[i]的情况，让strNum[i - 1]减一，但此时如果strNum[i - 1]减一了，可能又小于strNum[i - 2]。

这么说有点抽象，举个例子，数字：332，从前向后遍历的话，那么就把变成了329，此时2又小于了第一位的3了，真正的结果应该是299。

所以从前后向遍历会改变已经遍历过的结果！

那么从后向前遍历，就可以重复利用上次比较得出的结果了，从后向前遍历332的数值变化为：332 -> 329 -> 299

确定了遍历顺序之后，那么此时局部最优就可以推出全局，找不出反例，试试贪心。

https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0738.%E5%8D%95%E8%B0%83%E9%80%92%E5%A2%9E%E7%9A%84%E6%95%B0%E5%AD%97.md
"""

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        a = list(str(n))
        for i in range(len(a)-1,0,-1):
            if int(a[i]) < int(a[i-1]):
                a[i-1] = str(int(a[i-1]) - 1)
                a[i:] = '9' * (len(a) - i)  #python不需要设置flag值，直接按长度给9就好了
        print(a)
        return int("".join(a))

if __name__ == '__main__':
    res = Solution().monotoneIncreasingDigits(10)
    print(res)