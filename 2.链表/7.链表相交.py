#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :7.链表相交.py
# @Time     :2022/2/14 上午10:31
# @Author   :Chang Qing
 
"""
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。

思路：
方法一： 快慢法则
方法二： 双指针，先求出两链表的长度，然后尾巴对齐，长链表先跑
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        根据快慢法则，走的快的一定会追上走得慢的。
        在这道题里，有的链表短，他走完了就去走另一条链表，我们可以理解为走的快的指针。

        那么，只要其中一个链表走完了，就去走另一条链表的路。如果有交点，他们最终一定会在同一个
        位置相遇
        """
        cur_a, cur_b = headA, headB  # 用两个指针代替a和b

        while cur_a != cur_b:
            cur_a = cur_a.next if cur_a else headB  # 如果a走完了，那么就切换到b走
            cur_b = cur_b.next if cur_b else headA  # 同理，b走完了就切换到a

        return cur_a