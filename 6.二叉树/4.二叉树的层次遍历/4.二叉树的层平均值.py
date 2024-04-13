#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :1.二叉树层次遍历.py
# @Time     :2022/2/16 下午7:56
# @Author   :Chang Qing
 

"""
leetcode 637
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。


思路：
层序遍历的时候，判断是否遍历到单层的最后面的元素，如果是，就放进result数组中，随后返回result就可以了。
"""


class Solution:
    """二叉树层平均值迭代解法"""

    def averageOfLevels(self, root: TreeNode) -> List[float]:
        results = []
        if not root:
            return results

        from collections import deque
        que = deque([root])

        while que:
            size = len(que)
            sum_ = 0
            for _ in range(size):
                cur = que.popleft()
                sum_ += cur.val
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            results.append(sum_ / size)

        return results