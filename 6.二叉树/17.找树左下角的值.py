#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :15.找树左下角的值.py
# @Time     :2022/2/17 下午3:03
# @Author   :Chang Qing
 
"""
leetcode 513
给定一个二叉树，在树的最后一行找到最左边的值。

"""

# 递归:
# https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0513.%E6%89%BE%E6%A0%91%E5%B7%A6%E4%B8%8B%E8%A7%92%E7%9A%84%E5%80%BC.md
"""
咋眼一看，这道题目用递归的话就就一直向左遍历，最后一个就是答案呗？

没有这么简单，一直向左遍历到最后一个，它未必是最后一行啊。

我们来分析一下题目：在树的最后一行找到最左边的值。

首先要是最后一行，然后是最左边的值。

如果使用递归法，如何判断是最后一行呢，其实就是深度最大的叶子节点一定是最后一行。

如果对二叉树深度和高度还有点疑惑的话，请看：110.平衡二叉树。

所以要找深度最大的叶子节点。

那么如果找最左边的呢？可以使用前序遍历，这样才先优先左边搜索，然后记录深度最大的叶子节点，此时就是树的最后一行最左边的值。"""
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        max_depth = -float("INF")
        leftmost_val = 0

        def __traverse(root, cur_depth):
            nonlocal max_depth, leftmost_val
            if not root.left and not root.right:
                if cur_depth > max_depth:
                    max_depth = cur_depth
                    leftmost_val = root.val
            if root.left:
                cur_depth += 1
                __traverse(root.left, cur_depth)
                cur_depth -= 1
            if root.right:
                cur_depth += 1
                __traverse(root.right, cur_depth)
                cur_depth -= 1

        __traverse(root, 0)
        return leftmost_val
# 迭代 - 层序遍历:

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = deque()
        if root:
            queue.append(root)
        result = 0
        while queue:
            q_len = len(queue)
            for i in range(q_len):
                if i == 0:
                    result = queue[i].val
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return result