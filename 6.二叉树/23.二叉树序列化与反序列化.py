#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :23.二叉树序列化与反序列化.py
# @Time     :2022/11/9 上午11:38
# @Author   :Chang Qing


"""
题目描述
    请实现两个函数，分别用来序列化和反序列化二叉树

解题思路：
  序列化二叉树：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串。需要注意的是，
      序列化二叉树的过程中，如果遇到空节点，需要以某种符号（这里用#）表示。以下图二叉树为例，序列化二叉树时，需要将空节点也存入字符串中。
      序列化二叉树：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串。需要注意的是，序列化二叉树的过程中，如果遇到空节点，
      需要以某种符号（这里用#）表示。以下图二叉树为例，序列化二叉树时，需要将空节点也存入字符串中。

  反序列化二叉树：根据某种遍历顺序得到的序列化字符串，重构二叉树。具体思路是按前序遍历“根左右”的顺序，根节点位于其左右子节点的前面，
      即非空（#）的第一个节点是某子树的根节点，左右子节点在该根节点后，以空节点#为分隔符。代码如下：
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        if not root:
            return '#'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)

    def Deserialize(self, s):
        # write code heredef Deserialize(self, s):
        list = s.split(',')
        return self.deserializeTree(list)

    def deserializeTree(self, list):
        if len(list) <= 0:
            return None
        val = list.pop(0)
        root = None
        if val != '#':
            root = TreeNode(int(val))
            root.left = self.deserializeTree(list)
            root.right = self.deserializeTree(list)
        return root