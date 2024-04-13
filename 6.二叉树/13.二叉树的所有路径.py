#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :13.二叉树的所有路径.py
# @Time     :2022/2/17 上午11:42
# @Author   :Chang Qing
 
"""
leetcode 257
给定一个二叉树，返回所有从根节点到叶子节点的路径。
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0257.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%89%80%E6%9C%89%E8%B7%AF%E5%BE%84.md
"""

# 递归法 + 隐形回溯


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        if not root:
            return []
        path = [str(root.val)]
        self.traversal(root, res, path)
        new_res = []
        for path in res:
            new_res.append("->".join(path))
        return new_res

    def traversal(self, root, res, path):
        if root.left == None and root.right == None:
            res.append(path[:])
        if root.left:
            path.append(str(root.left.val))
            self.traversal(root.left, res, path)
            path.pop()
        if root.right:
            path.append(str(root.right.val))
            self.traversal(root.right, res, path)
            path.pop()


# 迭代法：

from collections import deque


class Solution:
    """二叉树的所有路径 迭代法"""

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # 题目中节点数至少为1
        stack, path_st, result = deque([root]), deque(), []
        path_st.append(str(root.val))

        while stack:
            cur = stack.pop()
            path = path_st.pop()
            # 如果当前节点为叶子节点，添加路径到结果中
            if not (cur.left or cur.right):
                result.append(path)
            if cur.right:
                stack.append(cur.right)
                path_st.append(path + '->' + str(cur.right.val))
            if cur.left:
                stack.append(cur.left)
                path_st.append(path + '->' + str(cur.left.val))

        return result