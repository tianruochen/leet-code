#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :6.对称二叉树.py
# @Time     :2022/2/17 上午10:32
# @Author   :Chang Qing
 

"""
leetcode 100
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
https://coordinate.blog.csdn.net/article/details/81589007
"""
# 递归法:


class Solution:

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        if p == None and q == None:
            return True
        else:
            return False

    def isSameTree(self, p, q):
        # 首先排除空节点的情况
        if p == None and q != None:
            return False
        elif p != None and q == None:
            return False
        elif p == None and p == None:
            return True
        # 排除了空节点，再排除数值不相同的情况
        elif p.val != p.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.rigth, q.right)

# 迭代法： 使用队列

import collections


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        q = [(p, q)]
        while q:
            node1, node2 = q.pop(0)
            if node1 and node2 and node1.val == node2.val:
                q.append((node1.left, node2.left))
                q.append((node1.right, node2.right))
            else:
                if node1 != node2:  # node1 == None and node2 != None  node1 != None and node2 == None
                    return False

        return True
