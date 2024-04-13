#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :1.leetcode209.py
# @Time     :2022/2/10 下午7:22
# @Author   :Chang Qing
 
"""
https://blog.csdn.net/weixin_47896156/article/details/123027422
求最长

水果成篮
在一排树中，第 i 棵树产生 tree[i] 型的水果。
你可以从你选择的任何树开始，然后重复执行以下步骤：

把这棵树上的水果放进你的篮子里。如果你做不到，就停下来。
移动到当前树右侧的下一棵树。如果右边没有树，就停下来。
请注意，在选择一颗树后，你没有任何选择：你必须执行步骤 1，然后执行步骤 2，然后返回步骤 1，然后执行步骤 2，依此类推，直至停止。

你有两个篮子，每个篮子可以携带任何数量的水果，但你希望每个篮子只携带一种类型的水果。
用这个程序最多你能收集几颗水果树？

思路分析：
    构造一个虚拟的窗口[left, right)，当窗口tree[left, right)中的水果种数不多于2时，扩大右边界，此时窗口的大小就是可获取的水果种数，否则窗口中的水果种数超过2，则缩小左边界。


窗口内是什么？
如何移动窗口的起始位置？
如何移动窗口的结束位置？
reference：
https://blog.csdn.net/qq_41855420/article/details/92836075
"""

class Solution:
    def totalFruit(self, nums) -> int:
        res = 0
        index = 0   # 记录起始位置
        for i in range(len(nums)):
            count = len(set(nums[index:i+1]))
            while count > 2:
                index += 1
                count = len(set(nums[index:i]))
            res = max(res, i - index + 1)

        return res

    def totalFruit2(self, tree):  # 使用hash表来统计数量
        if len(tree) == 0:
            return 0
        if len(tree) <= 2:
            return len(tree)
        start = 0  # 滑动窗口左端
        max_num = 0  # 用于计算最大值
        from collections import defaultdict
        hash = defaultdict(int)  # 用于存放当前获得的水果的种类
        for i in range(len(tree)):
            hash[tree[i]] += 1  # 遍历tree数组，将当前树水果加入到hash中
            print(hash)
            while len(hash) > 2:
                hash[tree[start]] -= 1
                if hash[tree[start]] == 0:
                    del hash[tree[start]]
                start += 1
            max_num = max(max_num, i - start + 1)
            print(max_num)
        return max_num


if __name__ == '__main__':
    nums = [3,3,3,1,2,1,1,2,3,3,4]
    nums = [1,2,1]
    nums = [0,1,2,2]
    nums = [1,2,3,2,2]
    res = Solution().totalFruit(nums)
    print(res)