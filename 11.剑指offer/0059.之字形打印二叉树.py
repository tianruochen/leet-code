# 题目描述
#     请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
# 第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
#
# 解题思路：
#   层次化遍历二叉树，并用一个标记记录深度，根据深度决定是否逆序
#
# 成功方案：

class Solution:
    def Print(self, pRoot):
        # write code here
      
        if not pRoot: return []
        res = []
        queue = [pRoot]
        j = -1
        while queue:
            j += 1
            n = len(queue)
            temp = []
            for _ in range(n):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if j % 2:
                temp.reverse()
            res.append(temp)
        return res
