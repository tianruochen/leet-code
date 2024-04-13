# 题目描述
#   输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
# (注意: 在返回值的list中，数组长度大的数组靠前)
#
# 解题思路：迭代
#
# 成功方案：
#   1. -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class Solution:
#     # 返回二维列表，内部每个列表表示找到的路径
#
#     def FindPath(self, root, expectNumber):
#         # write code here
#         if not root:
#             return []
#         if root and not root.left and not root.right and root.val == expectNumber:
#             return [[root.val]]
#         res = []
#         left = self.FindPath(root.left, expectNumber - root.val)
#         right = self.FindPath(root.right, expectNumber - root.val)
#         for i in left + right:
#             res.append([root.val] + i)
#         return res


# 2.先序遍历：
#
#     每次访问一个节点，那么就将当前权值求和
#     如果当前权值和与期待的和一致，那么说明我们找到了一个路径，保存或者输出
#     每次深度遍历到底部，回退一个点

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.result_all = []
        self.array = []

    def FindPath(self, root, expectNumber):
        # write code here
        if not root: return []
        self.array.append(root.val)
        expectNumber -= root.val
        if expectNumber == 0 and not root.left and not root.right:
            self.result_all.append(self.array[:])  # 一定要用深拷贝
        self.FindPath(root.left, expectNumber)
        self.FindPath(root.right, expectNumber)
        self.array.pop()
        return self.result_all
