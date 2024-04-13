#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :7.填充每个节点的下一个右侧节点指针.py
# @Time     :2022/2/16 下午8:43
# @Author   :Chang Qing
 

"""leetcode 116
给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL

思路:

本题依然是层序遍历，只不过在单层遍历的时候记录一下本层的头部节点，然后在遍历的时候让前一个节点指向本节点就可以了
"""
# 层序遍历解法
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = [root]
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == n - 1:
                    break
                node.next = queue[0]
        return root

# 链表解法
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        first = root
        while first:
            cur = first
            while cur:  # 遍历每一层的节点
                if cur.left: cur.left.next = cur.right  # 找左节点的next
                if cur.right and cur.next: cur.right.next = cur.next.left  # 找右节点的next
                cur = cur.next # cur同层移动到下一节点
            first = first.left  # 从本层扩展到下一层
        return root