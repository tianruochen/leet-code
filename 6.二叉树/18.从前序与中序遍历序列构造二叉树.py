#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :18.从中序与后序遍历序列构造二叉树.py
# @Time     :2022/2/17 下午3:54
# @Author   :Chang Qing
 

"""
leetcode 105
根据一棵树的中序遍历与后序遍历构造二叉树。

注意: 你可以假设树中没有重复的元素。
思路：
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0106.%E4%BB%8E%E4%B8%AD%E5%BA%8F%E4%B8%8E%E5%90%8E%E5%BA%8F%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97%E6%9E%84%E9%80%A0%E4%BA%8C%E5%8F%89%E6%A0%91.md

"""


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 第一步: 特殊情况讨论: 树为空. 或者说是递归终止条件
        if not preorder:
            return None

        # 第二步: 前序遍历的第一个就是当前的中间节点.
        root_val = preorder[0]
        root = TreeNode(root_val)

        # 第三步: 找切割点.
        separator_idx = inorder.index(root_val)

        # 第四步: 切割inorder数组. 得到inorder数组的左,右半边.
        inorder_left = inorder[:separator_idx]
        inorder_right = inorder[separator_idx + 1:]

        # 第五步: 切割preorder数组. 得到preorder数组的左,右半边.
        # ⭐️ 重点1: 中序数组大小一定跟前序数组大小是相同的.
        preorder_left = preorder[1:1 + len(inorder_left)]
        preorder_right = preorder[1 + len(inorder_left):]

        # 第六步: 递归
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root