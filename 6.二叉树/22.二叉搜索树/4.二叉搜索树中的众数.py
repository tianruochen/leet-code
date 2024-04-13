#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :4.二叉搜索树中的众数.py
# @Time     :2022/2/17 下午5:52
# @Author   :Chang Qing
 

"""
leetcode 501
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：

结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0501.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E4%BC%97%E6%95%B0.md
"""

# 递归法
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre = TreeNode()
        self.count = 0
        self.max_count = 0
        self.result = []

    def findMode(self, root: TreeNode) -> List[int]:
        if not root: return None
        self.search_BST(root)
        return self.result

    def search_BST(self, cur: TreeNode) -> None:
        if not cur: return None
        self.search_BST(cur.left)
        # 第一个节点
        if not self.pre:
            self.count = 1
        # 与前一个节点数值相同
        elif self.pre.val == cur.val:
            self.count += 1
            # 与前一个节点数值不相同
        else:
            self.count = 1
        self.pre = cur

        if self.count == self.max_count:
            self.result.append(cur.val)

        if self.count > self.max_count:
            self.max_count = self.count
            self.result = [cur.val]  # 清空self.result，确保result之前的的元素都失效

        self.search_BST(cur.right)

# 迭代法-中序遍历-不使用额外空间，利用二叉搜索树特性
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        stack = []
        cur = root
        pre = None
        maxCount, count = 0, 0
        res = []
        while cur or stack:
            if cur:  # 指针来访问节点，访问到最底层
                stack.append(cur)
                cur = cur.left
            else:  # 逐一处理节点
                cur = stack.pop()
                if pre == None:  # 第一个节点
                    count = 1
                elif pre.val == cur.val:  # 与前一个节点数值相同
                    count += 1
                else:                     # 与前一个节点数值不同
                    count = 1
                if count == maxCount:     # count 与maxcount 的关系
                    res.append(cur.val)
                if count > maxCount:
                    maxCount = count
                    res.clear()
                    res.append(cur.val)

                pre = cur
                cur = cur.right
        return res
