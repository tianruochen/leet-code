#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :2.01背包(滚动数组).py
# @Time     :2022/3/9 下午9:57
# @Author   :Chang Qing
 

"""
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E8%83%8C%E5%8C%85%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%8001%E8%83%8C%E5%8C%85-2.md
"""
def test_1_wei_bag_problem():
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bag_weight = 4
    # 初始化: 全为0
    dp = [0] * (bag_weight + 1)

    # 先遍历物品, 再遍历背包容量
    for i in range(len(weight)):
        for j in range(bag_weight, weight[i] - 1, -1):
            # 递归公式
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

    print(dp)

test_1_wei_bag_problem()

def test(weight, value, bag):
    dp = [0] * bag +1
    for i in range(len(value)):
        for j in range(bag, weight[i]-1, -1):
            dp[j] = max(dp[j], dp[j-weight[i]]+value[i])