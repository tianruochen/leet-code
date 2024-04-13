#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :8.删除二叉搜索树中的节点.py
# @Time     :2022/2/18 上午11:33
# @Author   :Chang Qing
 

"""
leetcode 450
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：
首先找到需要删除的节点； 如果找到了，删除它。 说明： 要求算法时间复杂度为 $O(h)$，h 为树的高度。

思路：
这里就把平衡二叉树中删除节点遇到的情况都搞清楚。

有以下五种情况：

第一种情况：没找到删除的节点，遍历到空节点直接返回了
找到删除的节点
第二种情况：左右孩子都为空（叶子节点），直接删除节点， 返回NULL为根节点
第三种情况：删除节点的左孩子为空，右孩子不为空，删除节点，右孩子补位，返回右孩子为根节点
第四种情况：删除节点的右孩子为空，左孩子不为空，删除节点，左孩子补位，返回左孩子为根节点
第五种情况：左右孩子节点都不为空，则将删除节点的左子树头结点（左孩子）放到删除节点的右子树的最左面节点的左孩子上，返回删除节点右孩子为新的根节点。
"""

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return root  #第一种情况：没找到删除的节点，遍历到空节点直接返回了
        if root.val == key:
            if not root.left and not root.right:  #第二种情况：左右孩子都为空（叶子节点），直接删除节点， 返回NULL为根节点
                del root
                return None
            if not root.left and root.right:  #第三种情况：其左孩子为空，右孩子不为空，删除节点，右孩子补位 ，返回右孩子为根节点
                tmp = root
                root = root.right
                del tmp
                return root
            if root.left and not root.right:  #第四种情况：其右孩子为空，左孩子不为空，删除节点，左孩子补位，返回左孩子为根节点
                tmp = root
                root = root.left
                del tmp
                return root
            else:  #第五种情况：左右孩子节点都不为空，则将删除节点的左子树放到删除节点的右子树的最左面节点的左孩子的位置
                v = root.right
                while v.left:
                    v = v.left
                v.left = root.left
                tmp = root
                root = root.right
                del tmp
                return root
        if root.val > key: root.left = self.deleteNode(root.left,key)  #左递归
        if root.val < key: root.right = self.deleteNode(root.right,key)  #右递归
        return root


"""
普通二叉树的删除方式
这里我在介绍一种通用的删除，普通二叉树的删除方式（没有使用搜索树的特性，遍历整棵树），用交换值的操作来删除目标节点。

代码中目标节点（要删除的节点）被操作了两次：

第一次是和目标节点的右子树最左面节点交换。
第二次直接被NULL覆盖了。
思路有点绕，感兴趣的同学可以画图自己理解一下。

代码如下：（关键部分已经注释）

class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (root == nullptr) return root;
        if (root->val == key) {
            if (root->right == nullptr) { // 这里第二次操作目标值：最终删除的作用
                return root->left;
            }
            TreeNode *cur = root->right;
            while (cur->left) {
                cur = cur->left;
            }
            swap(root->val, cur->val); // 这里第一次操作目标值：交换目标值其右子树最左面节点。
        }
        root->left = deleteNode(root->left, key);
        root->right = deleteNode(root->right, key);
        return root;
    }
};
"""