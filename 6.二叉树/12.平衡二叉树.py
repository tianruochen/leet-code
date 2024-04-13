#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :12.平衡二叉树.py
# @Time     :2022/2/17 上午11:27
# @Author   :Chang Qing
 
"""
leetcode 110
平衡二叉树
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1
"""

# 递归法：

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        left_depth = self.get_depth(root.left)
        right_depth = self.get_depth(root.right)
        if abs(left_depth - right_depth) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def get_depth(self, root):
        if not root:
            return 0
        left_depth = self.get_depth(root.left)
        right_depth = self.get_depth(root.right)
        return 1 + max(left_depth, right_depth)

# 迭代法：

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        st = []
        if not root:
            return True
        st.append(root)
        while st:
            node = st.pop()  # 中
            if abs(self.getDepth(node.left) - self.getDepth(node.right)) > 1:
                return False
            if node.right:
                st.append(node.right)  # 右（空节点不入栈）
            if node.left:
                st.append(node.left)  # 左（空节点不入栈）
        return True

    def getDepth(self, node):
        if not node:
            return 0
        leftdepth = self.getdepth(node.left)  # 左
        rightdepth = self.getdepth(node.right)  # 右
        depth = 1 + max(leftdepth, rightdepth)  # 中
        return depth
