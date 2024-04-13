#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :4.反转链表.py
# @Time     :2022/2/11 下午5:53
# @Author   :Chang Qing


# 双指针 头插
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        pre = ListNode()
        # pre.next = head
        while (cur != None):
            temp = cur.next  # 保存一下 cur的下一个节点，因为接下来要改变cur->next
            cur.next = pre.next  # 反转
            # 更新pre、cur指针
            pre.next = cur
            cur = temp
        return pre.next


"""
ListNode* reverseList(ListNode* head) {
    if(head==NULL || head->next==NULL)
        return head;
    ListNode *newHead=reverseList(head->next);
    head->next->next=head;
    head->next=NULL;
    return newHead;
}
"""
