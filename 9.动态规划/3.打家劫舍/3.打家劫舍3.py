#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :3.打家劫舍3.py
# @Time     :2022/3/24 下午4:38
# @Author   :Chang Qing
 

"""
leetcode 337
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。
一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

reference:
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0337.%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8DIII.md
"""

"""
暴力递归：
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right  is None:
            return root.val
        # 偷父节点
        val1 = root.val
        if root.left:
            val1 += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            val1 += self.rob(root.right.left) + self.rob(root.right.right)
        # 不偷父节点
        val2 = self.rob(root.left) + self.rob(root.right)
        return max(val1, val2)

"""
记忆化递归：
使用一个map把计算过的结果保存一下，这样如果计算过孙子了，那么计算孩子的时候可以复用孙子节点的结果。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    memory = {}
    def rob(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right  is None:
            return root.val
        if self.memory.get(root) is not None:
            return self.memory[root]
        # 偷父节点
        val1 = root.val
        if root.left:
            val1 += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            val1 += self.rob(root.right.left) + self.rob(root.right.right)
        # 不偷父节点
        val2 = self.rob(root.left) + self.rob(root.right)
        self.memory[root] = max(val1, val2)
        return max(val1, val2)


"""
动态规划:
1.确定递归函数的参数和返回值
这里我们要求一个节点 偷与不偷的两个状态所得到的金钱，那么返回值就是一个长度为2的数组。

参数为当前节点，代码如下：

vector<int> robTree(TreeNode* cur) {
其实这里的返回数组就是dp数组。

所以dp数组（dp table）以及下标的含义：下标为0记录不偷该节点所得到的的最大金钱，下标为1记录偷该节点所得到的的最大金钱。

所以本题dp数组就是一个长度为2的数组！

那么有同学可能疑惑，长度为2的数组怎么标记树中每个节点的状态呢？

别忘了在递归的过程中，系统栈会保存每一层递归的参数。

如果还不理解的话，就接着往下看，看到代码就理解了哈。

2.确定终止条件
在遍历的过程中，如果遇到空节点的话，很明显，无论偷还是不偷都是0，所以就返回

if (cur == NULL) return vector<int>{0, 0};
这也相当于dp数组的初始化

3.确定遍历顺序
首先明确的是使用后序遍历。 因为通过递归函数的返回值来做下一步计算。

通过递归左节点，得到左节点偷与不偷的金钱。
通过递归右节点，得到右节点偷与不偷的金钱。

代码如下：

// 下标0：不偷，下标1：偷
vector<int> left = robTree(cur->left); // 左
vector<int> right = robTree(cur->right); // 右
// 中
4.确定单层递归的逻辑
如果是偷当前节点，那么左右孩子就不能偷，val1 = cur->val + left[0] + right[0]; （如果对下标含义不理解就在回顾一下dp数组的含义）
如果不偷当前节点，那么左右孩子就可以偷，至于到底偷不偷一定是选一个最大的，所以：val2 = max(left[0], left[1]) + max(right[0], right[1]);
最后当前节点的状态就是{val2, val1}; 即：{不偷当前节点得到的最大金钱，偷当前节点得到的最大金钱}

代码如下：

vector<int> left = robTree(cur->left); // 左
vector<int> right = robTree(cur->right); // 右

// 偷cur
int val1 = cur->val + left[0] + right[0];
// 不偷cur
int val2 = max(left[0], left[1]) + max(right[0], right[1]);
return {val2, val1};
5.举例推导dp数组

https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0337.%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8DIII.md
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        result = self.rob_tree(root)
        return max(result[0], result[1])

    def rob_tree(self, node):
        if node is None:
            return (0, 0)  # (偷当前节点金额，不偷当前节点金额)
        left = self.rob_tree(node.left)
        right = self.rob_tree(node.right)
        val1 = node.val + left[1] + right[1]  # 偷当前节点，不能偷子节点
        val2 = max(left[0], left[1]) + max(right[0], right[1])  # 不偷当前节点，可偷可不偷子节点
        return (val1, val2)