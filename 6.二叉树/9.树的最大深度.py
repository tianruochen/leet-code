#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :9.二叉树的最大深度.py
# @Time     :2022/2/17 上午10:51
# @Author   :Chang Qing
 

"""
leetcode 104.二叉树的最大深度

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
"""
# 104.
# 二叉树的最大深度
# 递归法：

class solution:
    def maxdepth(self, root: treenode) -> int:

        if not node:
            return 0
        leftdepth = self.maxdepth(root.left)  # 左
        rightdepth = self.maxdepth(root.right)  # 右
        return 1 + max(leftdepth, rightdepth)  # 中


# 递归法：精简代码


class solution:
    def maxdepth(self, root: treenode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxdepth(root.left), self.maxdepth(root.right))


# 迭代法：

import collections


class solution:
    def maxdepth(self, root: treenode) -> int:
        if not root:
            return 0
        depth = 0  # 记录深度
        queue = collections.deque()
        queue.append(root)
        while queue:
            size = len(queue)
            depth += 1
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth


# 559.
# n叉树的最大深度
# 递归法：

class solution:
    def maxdepth(self, root: 'node') -> int:
        if not root:
            return 0
        depth = 0
        for i in range(len(root.children)):
            depth = max(depth, self.maxdepth(root.children[i]))
        return depth + 1


# 迭代法：

import collections


class solution:
    def maxdepth(self, root: 'node') -> int:
        queue = collections.deque()
        if root:
            queue.append(root)
        depth = 0  # 记录深度
        while queue:
            size = len(queue)
            depth += 1
            for i in range(size):
                node = queue.popleft()
                for j in range(len(node.children)):
                    if node.children[j]:
                        queue.append(node.children[j])
        return depth


# 使用栈来模拟后序遍历依然可以


class solution:
    def maxdepth(self, root: 'node') -> int:
        st = []
        if root:
            st.append(root)
        depth = 0
        result = 0
        while st:
            node = st.pop()
            if node != none:
                st.append(node)  # 中
                st.append(none)
                depth += 1
                for i in range(len(node.children)):  # 处理孩子
                    if node.children[i]:
                        st.append(node.children[i])

            else:
                node = st.pop()
                depth -= 1
            result = max(result, depth)
        return result