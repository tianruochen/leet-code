#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :18.从中序与后序遍历序列构造二叉树.py
# @Time     :2022/2/17 下午3:54
# @Author   :Chang Qing
 

"""
leetcode 106
根据一棵树的中序遍历与后序遍历构造二叉树。

注意: 你可以假设树中没有重复的元素。
思路：
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0106.%E4%BB%8E%E4%B8%AD%E5%BA%8F%E4%B8%8E%E5%90%8E%E5%BA%8F%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97%E6%9E%84%E9%80%A0%E4%BA%8C%E5%8F%89%E6%A0%91.md
来看一下一共分几步：

第一步：如果数组大小为零的话，说明是空节点了。

第二步：如果不为空，那么取后序数组最后一个元素作为节点元素。

第三步：找到后序数组最后一个元素在中序数组的位置，作为切割点

第四步：切割中序数组，切成中序左数组和中序右数组 （顺序别搞反了，一定是先切中序数组）

第五步：切割后序数组，切成后序左数组和后序右数组

第六步：递归处理左区间和右区间
"""


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # 第一步: 特殊情况讨论: 树为空. (递归终止条件)
        if not postorder:
            return None

        # 第二步: 后序遍历的最后一个就是当前的中间节点.
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # 第三步: 找切割点.
        separator_idx = inorder.index(root_val)

        # 第四步: 切割inorder数组. 得到inorder数组的左,右半边.
        inorder_left = inorder[:separator_idx]
        inorder_right = inorder[separator_idx + 1:]

        # 第五步: 切割postorder数组. 得到postorder数组的左,右半边.
        # ⭐️ 重点1: 中序数组大小一定跟后序数组大小是相同的.
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left): len(postorder) - 1]

        # 第六步: 递归
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        return root