#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :9.二叉树的最大深度.py
# @Time     :2022/2/16 下午9:10
# @Author   :Chang Qing
 

"""
leetcode 111
给定一个二叉树，找出其最小深度。

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        queue = [root]
        depth = 0
        while queue:
            size = len(queue)
            depth += 1
            for _ in range(size):
                node = queue.pop(0)
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return 0
