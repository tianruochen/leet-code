#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :11.把二叉搜索树转换为累加树.py
# @Time     :2022/2/18 下午4:02
# @Author   :Chang Qing
 
"""
leetcode 538 把二叉搜索树转换为累加树
给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。

提醒一下，二叉搜索树满足下列约束条件：

节点的左子树仅包含键 小于 节点键的节点。 节点的右子树仅包含键 大于 节点键的节点。 左右子树也必须是二叉搜索树。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre = TreeNode()

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        倒序累加替换：
        [2, 5, 13] -> [[2]+[1]+[0], [2]+[1], [2]] -> [20, 18, 13]
        '''
        self.traversal(root)
        return root

    def traversal(self, root: TreeNode) -> None:
        # 因为要遍历整棵树，所以递归函数不需要返回值
        # Base Case
        if not root:
            return None
        # 单层递归逻辑：中序遍历的反译 - 右中左
        self.traversal(root.right)  # 右

        # 中节点：用当前root的值加上pre的值
        root.val += self.pre.val    # 中
        self.pre = root

        self.traversal(root.left)   # 左

"""
迭代法
class Solution {
private:
    int pre; // 记录前一个节点的数值
    void traversal(TreeNode* root) {
        stack<TreeNode*> st;
        TreeNode* cur = root;
        while (cur != NULL || !st.empty()) {
            if (cur != NULL) {
                st.push(cur);
                cur = cur->right;   // 右
            } else {
                cur = st.top();     // 中
                st.pop();
                cur->val += pre;
                pre = cur->val;
                cur = cur->left;    // 左
            }
        }
    }
public:
    TreeNode* convertBST(TreeNode* root) {
        pre = 0;
        traversal(root);
        return root;
    }
};
"""

