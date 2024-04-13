# 题目描述
#   给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
#
#
# 解题思路：
# 如果一个节点有右子树，那么它的下一个节点就是它的右子树中的最左子节点。
# 接着我们分析一个节点没有右子树的情形：
# 如果结点是它父节点的左子节点，那么它的下一个节点就是它的父节点。
# 如果一个节点没有右子树，并且它还是它父节点的右子节点。我们可以沿着指向父节点的指针一直向上遍历，直到找到一个是它父节点的左子节点的节点。如果这样的节点存在，那么这个节点的父节点就是我们要找的下一个节点
class Solution:
    '''/分析二叉树的下一个节点，一共有以下情况：
        //1.二叉树为空，则返回空；
        //2.节点右孩子存在，则设置一个指针从该节点的右孩子出发，一直沿着指向左子结点的指针找到的叶子节点即为下一个节点；
        //3.节点不是根节点。如果该节点是其父节点的左孩子，则返回父节点；否则继续向上遍历其父节点的父节点，重复之前的判断，返回结果。'''

    def GetNext(self, pNode):
        if not pNode:
            return pNode
        if pNode.right:
            left1 = pNode.right
            while left1.left:
                left1 = left1.left
            return left1

        while pNode.next:
            tmp = pNode.next
            if tmp.left == pNode:
                return tmp
            pNode = tmp
