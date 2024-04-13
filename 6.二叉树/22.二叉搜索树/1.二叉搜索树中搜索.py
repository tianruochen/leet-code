#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :1.二叉搜索树中搜索.py
# @Time     :2022/2/17 下午5:06
# @Author   :Chang Qing
 

"""
leetcode 700
给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。

"""
# 递归法：

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # 为什么要有返回值:
        #   因为搜索到目标节点就要立即return，
        #   这样才是找到节点就返回（搜索某一条边），如果不加return，就是遍历整棵树了。

        if not root or root.val == val:
            return root

        if root.val > val:
            return self.searchBST(root.left, val)

        if root.val < val:
            return self.searchBST(root.right, val)
# 迭代法：

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root is not None:
            if val < root.val: root = root.left
            elif val > root.val: root = root.right
            else: return root
        return root