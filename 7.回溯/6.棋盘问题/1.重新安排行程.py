#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :1.重新安排行程.py
# @Time     :2022/3/3 下午3:45
# @Author   :Chang Qing
 
"""
给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，对该行程进行重新规划排序。
所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。

提示：

如果存在多种有效的行程，请你按字符自然排序返回最小的行程组合。例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前
所有的机场都用三个大写字母表示（机场代码）。
假定所有机票至少存在一种合理的行程。
所有的机票必须都用一次 且 只能用一次。
示例 1：

输入：[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
输出：["JFK", "MUC", "LHR", "SFO", "SJC"]
示例 2：

输入：[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
输出：["JFK","ATL","JFK","SFO","ATL","SFO"]
解释：另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"]。但是它自然排序更大更靠后。

https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0332.%E9%87%8D%E6%96%B0%E5%AE%89%E6%8E%92%E8%A1%8C%E7%A8%8B.md
"""
"""
注意函数返回值我用的是bool！

我们之前讲解回溯算法的时候，一般函数返回值都是void，这次为什么是bool呢？

因为我们只需要找到一个行程，就是在树形结构中唯一的一条通向叶子节点的路线
"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # defaultdic(list) 是为了方便直接append
        tickets_dict = defaultdict(list)
        for item in tickets:
            tickets_dict[item[0]].append(item[1])
        '''
        tickets_dict里面的内容是这样的
         {'JFK': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['JFK', 'SFO']})
        '''
        path = ["JFK"]
        def backtracking(start_point):
            # 终止条件
            if len(path) == len(tickets) + 1:
                return True
            tickets_dict[start_point].sort()
            for _ in tickets_dict[start_point]:
                #必须及时删除，避免出现死循环
                end_point = tickets_dict[start_point].pop(0)
                path.append(end_point)
                # 只要找到一个就可以返回了
                if backtracking(end_point):
                    return True
                path.pop()
                tickets_dict[start_point].append(end_point)

        backtracking("JFK")
        return path