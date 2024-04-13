#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :2.删除节点.py
# @Time     :2022/2/11 下午2:38
# @Author   :Chang Qing


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode(next=head)  # 添加一个虚拟节点
        cur = dummy_head
        while (cur.next != None):
            if (cur.next.val == val):
                cur.next = cur.next.next  # 删除cur.next节点

            cur = cur.next
        return dummy_head.next
