#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :7.填充每个节点的下一个右侧节点指针.py
# @Time     :2022/2/16 下午8:43
# @Author   :Chang Qing
 

"""leetcode 118
这道题目说是二叉树，但116题目说是完整二叉树，其实没有任何差别，一样的代码一样的逻辑一样的味道
"""
# 层序遍历解法
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = [root]
        while queue:  # 遍历每一层
            length = len(queue)
            tail = None # 每一层维护一个尾节点
            for i in range(length): # 遍历当前层
                curnode = queue.pop(0)
                if tail is None:      # 每一行第一个节点  直接作为尾节点
                    tail = curnode
                else:
                    tail.next = curnode # 让尾节点指向当前节点
                    tail = tail.next # 让当前节点成为尾节点
                if curnode.left : queue.append(curnode.left)
                if curnode.right: queue.append(curnode.right)
        return root

# 链表解法
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        first = root
        while first:  # 遍历每一层
            dummyHead = Node(None)  # 为下一行创建一个虚拟头节点，相当于下一行所有节点链表的头结点(每一层都会创建)；
            tail = dummyHead  # 为下一行维护一个尾节点指针（初始化是虚拟节点）
            cur = first
            while cur:  # 遍历当前层的节点
                if cur.left:  # 链接下一行的节点
                    tail.next = cur.left
                    tail = tail.next
                if cur.right:
                    tail.next = cur.right
                    tail = tail.next
                cur = cur.next  # cur同层移动到下一节点
            first = dummyHead.next  # 此处为换行操作，更新到下一行
        return root