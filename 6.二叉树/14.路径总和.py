#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :16.路径总和.py
# @Time     :2022/2/17 下午3:12
# @Author   :Chang Qing
 
"""
leetcode 112
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0112.%E8%B7%AF%E5%BE%84%E6%80%BB%E5%92%8C.md
"""

# 递归

class solution:
    def haspathsum(self, root: treenode, targetsum: int) -> bool:

        def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
            if not root:
                return False
            if not root.left and not root.right and targetSum - root.val == 0:
                return True
            return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)


    def haspathsum(self, root: treenode, targetsum: int) -> bool:
        def isornot(root, targetsum) -> bool:
            if (not root.left) and (not root.right) and targetsum == 0:
                return True  # 遇到叶子节点，并且计数为0
            if (not root.left) and (not root.right):
                return False  # 遇到叶子节点，计数不为0
            if root.left:
                targetsum -= root.left.val  # 左节点
                if isornot(root.left, targetsum): return True  # 递归，处理左节点
                targetsum += root.left.val  # 回溯
            if root.right:
                targetsum -= root.right.val  # 右节点
                if isornot(root.right, targetsum): return True  # 递归，处理右节点
                targetsum += root.right.val  # 回溯
            return False

        if root == None:
            return False  # 别忘记处理空treenode
        else:
            return isornot(root, targetsum - root.val)
# 迭代 - 层序遍历

class solution:
    def haspathsum(self, root: treenode, targetsum: int) -> bool:
        if not root: 
            return False

        stack = []  # [(当前节点，路径数值), ...]
        stack.append((root, root.val))

        while stack: 
            cur_node, path_sum = stack.pop()

            if not cur_node.left and not cur_node.right and path_sum == targetsum: 
                return True

            if cur_node.right: 
                stack.append((cur_node.right, path_sum + cur_node.right.val))    

            if cur_node.left: 
                stack.append((cur_node.left, path_sum + cur_node.left.val))

        return False