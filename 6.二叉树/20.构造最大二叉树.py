#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :20.构造最大二叉树.py
# @Time     :2022/2/17 下午4:04
# @Author   :Chang Qing
 
"""
leetcode 654.最大二叉树
给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：

二叉树的根是数组中的最大元素。
左子树是通过数组中最大值左边部分构造出的最大二叉树。
右子树是通过数组中最大值右边部分构造出的最大二叉树。
通过给定的数组构建最大二叉树，并且输出这个树的根节点。

思路：
构造树一般采用的是前序遍历，因为先构造中间节点，然后递归构造左子树和右子树。
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0654.%E6%9C%80%E5%A4%A7%E4%BA%8C%E5%8F%89%E6%A0%91.md
"""


class Solution:
    """递归法 更快"""

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        maxvalue = max(nums)
        index = nums.index(maxvalue)

        root = TreeNode(maxvalue)

        left = nums[:index]
        right = nums[index + 1:]

        root.left = self.constructMaximumBinaryTree(left)
        root.right = self.constructMaximumBinaryTree(right)
        return root


class Solution:
    """最大二叉树 递归法"""

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.traversal(nums, 0, len(nums))

    def traversal(self, nums: List[int], begin: int, end: int) -> TreeNode:
        # 列表长度为0时返回空节点
        if begin == end:
            return None

        # 找到最大的值和其对应的下标
        max_index = begin
        for i in range(begin, end):
            if nums[i] > nums[max_index]:
                max_index = i

        # 构建当前节点
        root = TreeNode(nums[max_index])

        # 递归构建左右子树
        root.left = self.traversal(nums, begin, max_index)
        root.right = self.traversal(nums, max_index + 1, end)

        return root