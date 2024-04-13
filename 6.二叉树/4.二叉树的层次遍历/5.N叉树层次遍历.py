#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :1.二叉树层次遍历.py
# @Time     :2022/2/16 下午7:56
# @Author   :Chang Qing
 

"""
leetcode 429
给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。

"""


class Solution:
    """N叉树的层序遍历迭代法"""

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        results = []
        if not root:
            return results

        from collections import deque
        que = deque([root])

        while que:
            result = []
            for _ in range(len(que)):
                cur = que.popleft()
                result.append(cur.val)
                # cur.children 是 Node 对象组成的列表，也可能为 None
                if cur.children:
                    que.extend(cur.children)
            results.append(result)

        return results