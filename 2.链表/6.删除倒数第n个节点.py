#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :6.删除倒数第n个节点.py
# @Time     :2022/2/14 上午10:28
# @Author   :Chang Qing
 
"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

进阶：你能尝试使用一趟扫描实现吗？

思路：
双指针的经典应用，如果要删除倒数第n个节点，让fast移动n步，
然后让fast和slow同时移动，直到fast指向链表末尾。删掉slow所指向的节点就可以了。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        head_dummy = ListNode()
        head_dummy.next = head

        slow, fast = head_dummy, head_dummy
        while(n!=0): #fast先往前走n步
            fast = fast.next
            n -= 1
        while(fast.next!=None):
            slow = slow.next
            fast = fast.next
        #fast 走到结尾后，slow的下一个节点为倒数第N个节点
        slow.next = slow.next.next #删除
        return head_dummy.next