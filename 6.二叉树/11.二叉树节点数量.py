#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :11.二叉树节点数量.py
# @Time     :2022/2/17 上午11:26
# @Author   :Chang Qing


# 递归法：

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return self.getNodesNum(root)

    def getNodesNum(self, cur):
        if not cur:
            return 0
        leftNum = self.getNodesNum(cur.left)  # 左
        rightNum = self.getNodesNum(cur.right)  # 右
        treeNum = leftNum + rightNum + 1  # 中
        return treeNum


# 递归法：精简版


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


# 迭代法：

import collections


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        queue = collections.deque()
        if root:
            queue.append(root)
        result = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                result += 1  # 记录节点数量
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result