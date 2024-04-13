#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :9.二叉树的最大深度.py
# @Time     :2022/2/16 下午9:10
# @Author   :Chang Qing
 

"""
leetcode 104
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。
"""


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0

        queue_ = [root]
        result = []
        while queue_:
            length = len(queue_)
            sub = []
            for i in range(length):
                cur = queue_.pop(0)
                sub.append(cur.val)
                # 子节点入队列
                if cur.left: queue_.append(cur.left)
                if cur.right: queue_.append(cur.right)
            result.append(sub)

        return len(result)