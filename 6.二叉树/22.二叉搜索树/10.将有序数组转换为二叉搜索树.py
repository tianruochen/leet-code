#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :10.将有序数组转换为二叉搜索树.py
# @Time     :2022/2/18 下午3:55
# @Author   :Chang Qing
 

"""
leetcode 108.将有序数组转换为二叉搜索树
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        '''
        构造二叉树：重点是选取数组最中间元素为分割点，左侧是递归左区间；右侧是递归右区间
        必然是平衡树
        左闭右闭区间
        '''
        # 返回根节点
        root = self.traversal(nums, 0, len(nums) - 1)
        return root

    def traversal(self, nums: List[int], left: int, right: int) -> TreeNode:
        # Base Case
        if left > right:
            return None

        # 确定左右界的中心，防越界
        mid = left + (right - left) // 2
        # 构建根节点
        mid_root = TreeNode(nums[mid])
        # 构建以左右界的中心为分割点的左右子树
        mid_root.left = self.traversal(nums, left, mid - 1)
        mid_root.right = self.traversal(nums, mid + 1, right)

        # 返回由被传入的左右界定义的某子树的根节点
        return mid_root