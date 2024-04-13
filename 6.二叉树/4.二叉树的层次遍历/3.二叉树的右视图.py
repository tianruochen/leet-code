#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :1.二叉树层次遍历.py
# @Time     :2022/2/16 下午7:56
# @Author   :Chang Qing
 

"""
leetcode 199
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

思路：
层序遍历的时候，判断是否遍历到单层的最后面的元素，如果是，就放进result数组中，随后返回result就可以了。
"""


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        # deque来自collections模块，不在力扣平台时，需要手动写入
        # 'from collections import deque' 导入
        # deque相比list的好处是，list的pop(0)是O(n)复杂度，deque的popleft()是O(1)复杂度

        quene = deque([root])
        out_list = []

        while quene:
            # 每次都取最后一个node就可以了
            node = quene[-1]
            out_list.append(node.val)

            # 执行这个遍历的目的是获取下一层所有的node
            for _ in range(len(quene)):
                node = quene.popleft()
                if node.left:
                    quene.append(node.left)
                if node.right:
                    quene.append(node.right)

        return out_list