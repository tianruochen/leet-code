#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :1.leetcode209.py
# @Time     :2022/2/10 下午7:22
# @Author   :Chang Qing
 
"""

https://blog.csdn.net/weixin_47896156/article/details/123027422
求最短

给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。

示例：

输入：s = 7, nums = [2,3,1,2,4,3] 输出：2 解释：子数组 [4,3] 是该条件下的长度最小的子数组。


滑动窗口也可以理解为双指针法的一种！只不过这种解法更像是一个窗口的移动，所以叫做滑动窗口更适合一些。

在本题中实现滑动窗口，主要确定如下三点：

窗口内是什么？
如何移动窗口的起始位置？
如何移动窗口的结束位置？


窗口就是 满足其和 ≥ s 的长度最小的 连续 子数组。
窗口的起始位置如何移动：如果当前窗口的值大于s了，窗口就要向前移动了（也就是该缩小了）。
窗口的结束位置如何移动：窗口的结束位置就是遍历数组的指针，窗口的起始位置设置为数组的起始位置就可以了。

reference：
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0209.%E9%95%BF%E5%BA%A6%E6%9C%80%E5%B0%8F%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84.md
"""

class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        # 定义一个无限大的数
        res = float("inf")
        Sum = 0
        index = 0   # 记录起始位置
        for i in range(len(nums)):
            Sum += nums[i]
            while Sum >= s:
                res = min(res, i-index+1)
                Sum -= nums[index]
                index += 1
        return 0 if res==float("inf") else res


if __name__ == '__main__':
    nums = [2, 3, 1, 2, 4, 3]
    s = 7
    res = Solution().minSubArrayLen(7, nums)
    print(res)