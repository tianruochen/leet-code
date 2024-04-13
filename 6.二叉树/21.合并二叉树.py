#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :21.合并二叉树.py
# @Time     :2022/2/17 下午5:03
# @Author   :Chang Qing
 
"""
leetcode 617
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0617.%E5%90%88%E5%B9%B6%E4%BA%8C%E5%8F%89%E6%A0%91.md
"""
# 递归法 - 前序遍历


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        # 递归终止条件:
        #  但凡有一个节点为空, 就立刻返回另外一个. 如果另外一个也为None就直接返回None.
        if not root1:
            return root2
        if not root2:
            return root1
        # 上面的递归终止条件保证了代码执行到这里root1, root2都非空.
        root1.val += root2.val  # 中
        root1.left = self.mergeTrees(root1.left, root2.left)  # 左
        root1.right = self.mergeTrees(root1.right, root2.right)  # 右

        return root1  # ⚠️ 注意: 本题我们重复使用了题目给出的节点而不是创建新节点. 节省时间, 空间.


# 迭代法


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1

        queue = deque()
        queue.append(root1)
        queue.append(root2)

        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()
            # 更新queue
            # 只有两个节点都有左节点时, 再往queue里面放.
            if node1.left and node2.left:
                queue.append(node1.left)
                queue.append(node2.left)
            # 只有两个节点都有右节点时, 再往queue里面放.
            if node1.right and node2.right:
                queue.append(node1.right)
                queue.append(node2.right)

            # 更新当前节点. 同时改变当前节点的左右孩子.
            node1.val += node2.val
            if not node1.left and node2.left:
                node1.left = node2.left
            if not node1.right and node2.right:
                node1.right = node2.right

        return root1
