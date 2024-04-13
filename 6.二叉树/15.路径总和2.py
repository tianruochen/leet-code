#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :16.路径总和.py
# @Time     :2022/2/17 下午3:12
# @Author   :Chang Qing
 
"""
leetcode 113
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

着重看思路 什么时候递归有返回值 什么时候不需要返回值
再来看返回值，递归函数什么时候需要返回值？什么时候不需要返回值？这里总结如下三点：

如果需要搜索整棵二叉树且不用处理递归返回值，递归函数就不要返回值。（这种情况就是本文下半部分介绍的113.路径总和ii）
如果需要搜索整棵二叉树且需要处理递归返回值，递归函数就需要返回值。 （这种情况我们在236. 二叉树的最近公共祖先中介绍）
如果要搜索其中一条符合条件的路径，那么递归一定需要返回值，因为遇到符合条件的路径了就要及时返回。

https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0112.%E8%B7%AF%E5%BE%84%E6%80%BB%E5%92%8C.md"""

# 递归

递归

class solution:

    def pathsum(self, root: treenode, targetsum: int) -> list[list[int]]:

        def traversal(cur_node, remain):
            if not cur_node.left and not cur_node.right and remain == 0:
                result.append(path[:])
                return

            if cur_node.left:
                path.append(cur_node.left.val)
                remain -= cur_node.left.val
                traversal(cur_node.left, remain)
                path.pop()
                remain += cur_node.left.val

            if cur_node.right:
                path.append(cur_node.right.val)
                remain -= cur_node.right.val
                traversal(cur_node.right, remain)
                path.pop()
                remain += cur_node.right.val

        result, path = [], []
        if not root:
            return []
        path.append(root.val)
        traversal(root, targetsum - root.val)
        return result

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
      def __init__(self):
          self.result_all = []
          self.array = []
      def FindPath(self,root, expectNumber):
              # write code here
          if not root: return []
          self.array.append(root.val)
          expectNumber -= root.val
          if expectNumber == 0 and not root.left and not root.right:
              self.result_all.append(self.array[:])   #一定要用深拷贝
          self.FindPath(root.left, expectNumber)
          self.FindPath(root.right, expectNumber)
          self.array.pop()
          return self.result_all