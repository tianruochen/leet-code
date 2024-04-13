# 题目描述
#   给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。
#
#
# 解题思路：
#     二插排序树中序遍历结果是有序的
#
# 成功方案：
class Solution:
    # 返回对应节点TreeNode
    
    def KthNode(self, pRoot, k):
        # write code here
        global res
        res = []
        self.miditer(pRoot)
        l = len(res)
        if k>l or k<=0:
            return None
        return res[k-1]
        
    def miditer(self,pRoot):
        if not pRoot:
            return None
        self.miditer(pRoot.left)
        res.append(pRoot)
        self.miditer(pRoot.right)
        
