#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :6.对称二叉树.py
# @Time     :2022/2/17 上午10:32
# @Author   :Chang Qing
 

"""
leetcode 572
给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

思路：深度优先搜索

在这里，先分析题意：

一个二叉树若为另一个树的子树，则它含有与另外一个树的子树相同结构和节点值。
根据示例 2 可知，判断是否为子树，必须有完全相同结构和节点值。
以下 s、t 表示两个二叉树，题目要求判断 t 是否是 s 的子树

现在将题意转换为可实现代码书写的思路，判断两个树是否相等，那么下面的条件必须同时成立：

当前两个树根节点值相同；
s 的左子树与 t 的左子树相同；
s 的右子树与 t 的右子树相同。
根据上面的思路，本篇幅考虑使用深度优化搜索的方法，枚举 s 的每个节点，判断这个点的子树是否与 t 相等。使用深度优先搜索检查，从根出发，同步移动遍历两个树，判断相应的位置是否相等。
"""
# 递归法:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        # c 子树为空时，返回 False
        if not s:
            return False         # 这里必须是self.isSubtree  而不能是self.is_same
        # 返回 要么两颗树相等，要么t是s左子树的子树， 要么是s右子树的子树
        # 而不应该是 要么两颗树相等，要么t和s的左子树相等，要么和s的右子树相等 两个概念是不一样的
        return self.is_same(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def is_same(self, c, t):
        # 两个树都为空时，也认为是相同
        if (not c) and (not t):
            return True
        # 当其中一个树为空，但另外一个树不为空时，此时则为不同
        if (not c and t) or (c and not t):
            return False
        # 两个树都不为空，若值不同，也为不同
        if (c.val != t.val):
            return False
        # 上面的情况都不符合时，继续向下检查
        return self.is_same(c.left, t.left) and self.is_same(c.right, t.right)

