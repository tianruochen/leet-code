#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :1.多重背包.py
# @Time     :2022/3/24 下午3:26
# @Author   :Chang Qing
 


"""

reference:
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E8%83%8C%E5%8C%85%E9%97%AE%E9%A2%98%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80%E5%A4%9A%E9%87%8D%E8%83%8C%E5%8C%85.md
"""


def test_multi_pack1():
    '''版本一：改变物品数量为01背包格式'''
    weight = [1, 3, 4]
    value = [15, 20, 30]
    nums = [2, 3, 2]
    bag_weight = 10
    for i in range(len(nums)):
        # 将物品展开数量为1
        while nums[i] > 1:
            weight.append(weight[i])
            value.append(value[i])
            nums[i] -= 1

    dp = [0] * (bag_weight + 1)
    # 遍历物品
    for i in range(len(weight)):
        # 遍历背包
        for j in range(bag_weight, weight[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

    print(" ".join(map(str, dp)))


def test_multi_pack2():
    '''版本：改变遍历个数'''
    weight = [1, 3, 4]
    value = [15, 20, 30]
    nums = [2, 3, 2]
    bag_weight = 10

    dp = [0] * (bag_weight + 1)
    for i in range(len(weight)):
        for j in range(bag_weight, weight[i] - 1, -1):
            # 以上是01背包，加上遍历个数
            for k in range(1, nums[i] + 1):
                if j - k * weight[i] >= 0:
                    dp[j] = max(dp[j], dp[j - k * weight[i]] + k * value[i])

    print(" ".join(map(str, dp)))


if __name__ == '__main__':
    test_multi_pack1()
    test_multi_pack2()