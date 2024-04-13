# 题目描述
#   从上往下打印出二叉树的每个节点，同层节点从左至右打印。
#
#  解题思路：
#     借助队列
#
#  成功方案：


def PrintFromTopToBottom(self, root):
    # write code here
    l = []
    if not root:
        return []
    q = [root]
    while q:
        size = len(q)          # 每一层的数量
        for i in range(size):
            t = q.pop(0)
            l.append(t.val)

            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
    return l
