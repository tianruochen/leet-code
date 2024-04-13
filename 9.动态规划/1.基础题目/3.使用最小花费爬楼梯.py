#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :3.使用最小花费爬楼梯.py
# @Time     :2022/3/9 上午11:21
# @Author   :Chang Qing
 
"""
leetcode 746
数组的每个下标作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值 cost[i]（下标从 0 开始）。

每当你爬上一个阶梯你都要花费对应的体力值，一旦支付了相应的体力值，你就可以选择向上爬一个阶梯或者爬两个阶梯。

请你找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。

示例 1：

输入：cost = [10, 15, 20] 输出：15 解释：最低花费是从 cost[1] 开始，然后走两步即可到阶梯顶，一共花费 15 。  示例 2：

输入：cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1] 输出：6 解释：最低花费方式是从 cost[0] 开始，逐个经过那些 1 ，跳过 cost[3] ，一共花费 6 。

提示：

cost 的长度范围是 [2, 1000]。
cost[i] 将会是一个整型数据，范围为 [0, 999] 。

https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0746.%E4%BD%BF%E7%94%A8%E6%9C%80%E5%B0%8F%E8%8A%B1%E8%B4%B9%E7%88%AC%E6%A5%BC%E6%A2%AF.md
"""

"""class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        vector<int> dp(cost.size() + 1);
        dp[0] = 0; // 默认第一步都是不花费体力的
        dp[1] = 0;
        for (int i = 2; i <= cost.size(); i++) {
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]);
        }
        return dp[cost.size()];
    }
};
"""


# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         dp = [0] * (len(cost))
#         dp[0] = cost[0]
#         dp[1] = cost[1]
#         for i in range(2, len(cost)):
#             dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
#         return min(dp[len(cost) - 1], dp[len(cost) - 2])


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)  # 题目要求要跳到顶部， 所以是要跳出cost
        dp[0] = 0
        dp[1] = 0   #默认第一步都是不花费体力的
        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[len(cost)]