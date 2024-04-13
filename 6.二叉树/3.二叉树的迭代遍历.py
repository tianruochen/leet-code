#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :3.二叉树的迭代便利.py
# @Time     :2022/2/16 下午5:19
# @Author   :Chang Qing
 
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

"""
前序遍历（迭代法）
我们先看一下前序遍历。

前序遍历是中左右，每次先处理的是中间节点，那么先将根节点放入栈中，然后将右孩子加入栈，再加入左孩子。

为什么要先加入 右孩子，再加入左孩子呢？ 因为这样出栈的时候才是中左右的顺序。
"""
class Solution:
    def preorderTraversal(self, root: TreeNode):
        # 根结点为空则返回空列表
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            # 中结点先处理
            result.append(node.val)
            # 右孩子先入栈
            if node.right:
                stack.append(node.right)
            # 左孩子后入栈
            if node.left:
                stack.append(node.left)
        return result


"""
中序遍历（迭代法）
为了解释清楚，我说明一下 刚刚在迭代的过程中，其实我们有两个操作：

处理：将元素放进result数组中
访问：遍历节点
分析一下为什么刚刚写的前序遍历的代码，不能和中序遍历通用呢，因为前序遍历的顺序是中左右，先访问的元素是中间节点，要处理的元素也是中间节点，所以刚刚才能写出相对简洁的代码，因为要访问的元素和要处理的元素顺序是一致的，都是中间节点。

那么再看看中序遍历，中序遍历是左中右，先访问的是二叉树顶部的节点，然后一层一层向下访问，直到到达树左面的最底部，再开始处理节点（也就是在把节点的数值放进result数组中），这就造成了处理顺序和访问顺序是不一致的。

那么在使用迭代法写中序遍历，就需要借用指针的遍历来帮助访问节点，栈则用来处理节点上的元素。
"""
class Solution:
    def inorderTraversal(self, root: TreeNode):
        if not root:
            return []
        stack = []  # 不能提前将root结点加入stack中
        result = []
        cur = root
        while cur or stack:
            # 先迭代访问最底层的左子树结点
            if cur:
                stack.append(cur)
                cur = cur.left
            # 到达最左结点后处理栈顶结点
            else:
                cur = stack.pop()
                result.append(cur.val)
                # 取栈顶元素右结点
                cur = cur.right
        return result


"""
再来看后序遍历，先序遍历是中左右，后续遍历是左右中，那么我们只需要调整一下先序遍历的代码顺序，就变成中右左的遍历顺序，然后在反转result数组，输出的结果顺序就是左右中了
"""
class Solution:
    def postorderTraversal(self, root: TreeNode):
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            # 中结点先处理
            result.append(node.val)
            # 左孩子先入栈
            if node.left:
                stack.append(node.left)
            # 右孩子后入栈
            if node.right:
                stack.append(node.right)
        # 将最终的数组翻转
        return result[::-1]