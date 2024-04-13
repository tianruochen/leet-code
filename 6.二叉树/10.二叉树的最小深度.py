#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :10.二叉树的最小深度.py
# @Time     :2022/2/17 上午11:02
# @Author   :Chang Qing
 
"""
leetcode 111
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。
"""
# 递归法：

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        if not root.left:
            return 1+right_depth
        if not root.right:
            return 1 + left_depth
        return min(left_depth, right_depth) + 1

# 迭代法：

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        que = deque()
        que.append(root)
        res = 1

        while que:
            for _ in range(len(que)):
                node = que.popleft()
                # 当左右孩子都为空的时候，说明是最低点的一层了，退出
                if not node.left and not node.right:
                    return res
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)
            res += 1
        return res
