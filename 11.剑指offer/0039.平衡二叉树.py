# 题目描述
#   输入一棵二叉树，判断该二叉树是否是平衡二叉树。
#
# 解题关键：
#   1.空树是平衡二叉树
#   2.左右子树深度差小于等于1为平衡二叉树
#
# 成功方案：
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        if abs(self.TreeDepth(pRoot.left)-self.TreeDepth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
       
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot == None:
            return 0
        nLeft = self.TreeDepth(pRoot.left)
        nRight = self.TreeDepth(pRoot.right)
        return max(nLeft+1,nRight+1)#(nLeft+1 if nLeft > nRight else nRight +1)
