#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :1.二叉树层次遍历.py
# @Time     :2022/2/16 下午7:56
# @Author   :Chang Qing
 

"""
leetcode 515
您需要在二叉树的每一行中找到最大的值。


"""

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        queue = [root]
        out_list = []
        while queue:
            length = len(queue)
            in_list = []
            for _ in range(length):
                curnode = queue.pop(0)
                in_list.append(curnode.val)
                if curnode.left: queue.append(curnode.left)
                if curnode.right: queue.append(curnode.right)
            out_list.append(max(in_list))
        return out_list