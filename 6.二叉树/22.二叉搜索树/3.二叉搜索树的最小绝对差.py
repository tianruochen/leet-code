#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :3.二叉搜索树的最小绝对差.py
# @Time     :2022/2/17 下午5:47
# @Author   :Chang Qing
 

"""
leetcode 530
给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。
"""

# 递归


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        res = []
        r = float("inf")

        def buildaList(root):

            # 把二叉搜索树转换成有序数组
            if not root: return None
            buildaList(root.left) # 左
            res.append(root.val) # 中
            buildaList(root.right) # 右
            return res

        buildaList(root)
        for i in range(len(res) - 1):  #
        # 统计有序数组的最小差值
            r = min(abs(res[i] - res[i + 1]), r)


        return r


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        stack = []
        cur = root
        pre = None
        result = float('inf')
        while cur or stack:
            if cur:  # 指针来访问节点，访问到最底层
                stack.append(cur)
                cur = cur.left
            else:  # 逐一处理节点
                cur = stack.pop()
                if pre:  # 当前节点和前节点的值的差值
                    result = min(result, cur.val - pre.val)
                pre = cur
                cur = cur.right
        return result


