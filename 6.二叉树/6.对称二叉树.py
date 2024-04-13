#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :6.对称二叉树.py
# @Time     :2022/2/17 上午10:32
# @Author   :Chang Qing
 

"""
leetcode 对称二叉树
给定一个二叉树，检查它是否是镜像对称的。
reference：
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0101.%E5%AF%B9%E7%A7%B0%E4%BA%8C%E5%8F%89%E6%A0%91.md
"""
# 递归法:


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.compare(root.left, root.right)

    def compare(self, left, right):
        # 首先排除空节点的情况
        if left == None and right != None:
            return False
        elif left != None and right == None:
            return False
        elif left == None and right == None:
            return True
        # 排除了空节点，再排除数值不相同的情况
        elif left.val != right.val:
            return False

        return self.compare(left.left, right.right) and self.compare(left.right, right.left)

        # # 此时就是：左右节点都不为空，且数值相同的情况
        # # 此时才做递归，做下一层的判断
        # outside = self.compare(left.left, right.right)  # 左子树：左、 右子树：右
        # inside = self.compare(left.right, right.left)  # 左子树：右、 右子树：左
        # isSame = outside and inside  # 左子树：中、 右子树：中 （逻辑处理）
        # return isSame


# 迭代法： 使用队列

import collections


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = collections.deque()
        queue.append(root.left)  # 将左子树头结点加入队列
        queue.append(root.right)  # 将右子树头结点加入队列
        while queue:  # 接下来就要判断这这两个树是否相互翻转
            leftNode = queue.popleft()
            rightNode = queue.popleft()
            if not leftNode and not rightNode:  # 左节点为空、右节点为空，此时说明是对称的
                continue

            # 左右一个节点不为空，或者都不为空但数值不相同，返回false
            if not leftNode or not rightNode or leftNode.val != rightNode.val:
                return False
            queue.append(leftNode.left)  # 加入左节点左孩子
            queue.append(rightNode.right)  # 加入右节点右孩子
            queue.append(leftNode.right)  # 加入左节点右孩子
            queue.append(rightNode.left)  # 加入右节点左孩子
        return True


# 迭代法：使用栈

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        st = []  # 这里改成了栈
        st.append(root.left)
        st.append(root.right)
        while st:
            leftNode = st.pop()
            rightNode = st.pop()
            if not leftNode and not rightNode:
                continue
            if not leftNode or not rightNode or leftNode.val != rightNode.val:
                return False
            st.append(leftNode.left)
            st.append(rightNode.right)
            st.append(leftNode.right)
            st.append(rightNode.left)
        return True