#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :12.二叉搜索树的.py
# @Time     :2022/11/8 上午11:54
# @Author   :Chang Qing

# 题目描述
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes, 否则输出No。假设输入的数组的任意两个数字都互不相同。
#
# 解题思路：
# 二插搜索树即二插排序树：的后序序列的合法序列是，对于一个序列S，最后一个元素是x （也就是根），如果去掉最后一个元素的序列为T，那么T满足：
# T可以分成两段，前一段（左子树）小于x，后一段（右子树）大于x，且这两段（子树）都是合法的后序序列。完美的递归定义
#
# 成功方案：
# 1.


def VerifySquenceOfBST(self, sequence):
    # write code here
    if len(sequence) <= 1:
        return True
    length = len(sequence)
    root = sequence[length - 1]
    # 在二叉搜索 树中 左子树节点小于根节点
    for i in range(length):
        if sequence[i] > root:
            break
    # 二叉搜索树中右子树的节点都大于根节点
    for j in range(i, length):
        if sequence[j] < root:
            return False
    # 判断左子树是否为二叉树
    left = self.VerifySquenceOfBST(sequence[0:i])
    # 判断 右子树是否为二叉树
    right = self.VerifySquenceOfBST(sequence[i:-1])
    return left and right
