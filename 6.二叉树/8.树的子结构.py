#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :6.对称二叉树.py
# @Time     :2022/2/17 上午10:32
# @Author   :Chang Qing
 

# 题目描述
#   输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
#
# 解决思路：递归
#
# 成功方案：
#
# 注意和上一题的区别，子树一定是子结构，但子结构不一定是子树  子树是一定要到叶子结点的

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:

    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        return self.is_subtree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)

    def is_subtree(self, c, t):
        if not t:                # 与两颗树相同不一样，子结构只需要t为None即可返回True, 子结构不需要到叶子结点
            return True
        if t and not c:
            return False
        if c.val != t.val:
            return False                  # 一定是and 不能是or
        return self.is_subtree(c.left,t.left) and self.is_subtree(c.right, t.right)

    def is_same(self, c, t):
        # 两个树都为空时，也认为是相同
        if (not c) and (not t):
            return True
        # 当其中一个树为空，但另外一个树不为空时，此时则为不同
        if (not c and t) or (c and not t):
            return False
        # 两个树都不为空，若值不同，也为不同
        if (c.val != t.val):
            return False
        # 上面的情况都不符合时，继续向下检查
        return self.is_same(c.left, t.left) and self.is_same(c.right, t.right)
