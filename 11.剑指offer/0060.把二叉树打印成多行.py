# 题目描述
#   从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
#
#
# 解题思路：
#   层次化遍历二叉树，每一层统计节点个数
#
# 成功方案：
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if pRoot == None:
            return [] 
        deque = [pRoot]
        result = []
        while deque:
            n = len(deque)
            temp = []
            for _ in range(n):
                node = deque.pop(0)
                temp.append(node.val)
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
            result.append(temp)
        return result
