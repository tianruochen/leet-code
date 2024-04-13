#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :9.复杂链表的复制.py
# @Time     :2022/11/8 下午4:02
# @Author   :Chang Qing
 

# 题目描述：
#       输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
# （注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
#
# 解题思路：
#       方案1：
#
#             第一步：遍历老链表，构建正常的链表，用一个map记录p到new_p
#             第二步：新老链表同步next移动，对比记录random指针。
#             p 1->2->3->4 map | | | | new_p 1->2->3->4
#
#             需要借助O(n)的空间，时间复杂度为o(n)


# 成功方案：
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead: return None
        p = pHead
        new_h = RandomListNode(p.label)
        pre_p = new_h
        random_map = {pHead: new_h}
        p = p.next
        while p:
            new_p = RandomListNode(p.label)
            random_map[p] = new_p
            pre_p.next = new_p
            pre_p = pre_p.next
            p = p.next
        p = pHead
        new_p = new_h
        while p:
            random_p = p.random
            if random_p:
                new_p.random = random_map[random_p]

            p = p.next
            new_p = new_p.next

        return new_h