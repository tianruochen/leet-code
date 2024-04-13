#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :2.验证二叉搜索树.py
# @Time     :2022/2/17 下午5:36
# @Author   :Chang Qing
 

"""
leetcode 98 验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

思路：
要知道中序遍历下，输出的二叉搜索树节点的数值是有序序列。
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0098.%E9%AA%8C%E8%AF%81%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.md
"""


# 递归 - 利用BST中序遍历特性, 把树
# "压缩"
# 成数组


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 思路: 利用BST中序遍历的特性.
        # 中序遍历输出的二叉搜索树节点的数值是有序序列
        candidate_list = []

        def __traverse(root: TreeNode) -> None:
            # nonlocal candidate_list
            if not root:
                return
            __traverse(root.left)
            candidate_list.append(root.val)
            __traverse(root.right)

        def __is_sorted(nums: list) -> bool:
            for i in range(1, len(nums)):
                if nums[i] <= nums[i - 1]:  # ⚠️ 注意: Leetcode定义二叉搜索树中不能有重复元素
                    return False
            return True

        __traverse(root)
        res = __is_sorted(candidate_list)

        return res


# 递归 - 标准做法


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 规律: BST的中序遍历节点数值是从小到大.
        cur_max = -float("INF")

        def __isValidBST(root: TreeNode) -> bool:
            nonlocal cur_max

            if not root:
                return True

            is_left_valid = __isValidBST(root.left)
            if cur_max < root.val:
                cur_max = root.val
            else:
                return False
            is_right_valid = __isValidBST(root.right)

            return is_left_valid and is_right_valid

        return __isValidBST(root)


# 迭代 - 中序遍历


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        cur = root
        pre = None
        while cur or stack:
            if cur:  # 指针来访问节点，访问到最底层
                stack.append(cur)
                cur = cur.left
            else:  # 逐一处理节点
                cur = stack.pop()
                if pre and cur.val <= pre.val:  # 比较当前节点和前节点的值的大小
                    return False
                pre = cur
                cur = cur.right
        return True