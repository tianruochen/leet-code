# 题目描述
#   请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
#
# 解题思路：
#   思路：首先根节点以及其左右子树，左子树的左子树和右子树的右子树相同
#         * 左子树的右子树和右子树的左子树相同即可，采用递归
#
# 成功方案：
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here

        def is_same(p1,p2):
            if not p1 and not p2:
                return True
            if (p1 and p2) and p1.val==p2.val:
                return is_same(p1.left,p2.right) and is_same(p1.right,p2.left)
            return False
        
        if not pRoot:
            return True
        return is_same(pRoot.left,pRoot.right)
        
        
# public class Solution {
#     boolean isSymmetrical(TreeNode pRoot)
#     {
#         if(pRoot == null){
#             return true;
#         }
#         return comRoot(pRoot.left, pRoot.right);
#     }
#     private boolean comRoot(TreeNode left, TreeNode right) {
#         // TODO Auto-generated method stub
#         if(left == null) return right==null;
#         if(right == null) return false;
#         if(left.val != right.val) return false;
#         return comRoot(left.right, right.left) && comRoot(left.left, right.right);
#     }
# }
