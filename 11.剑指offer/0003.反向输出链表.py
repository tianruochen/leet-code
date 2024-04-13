# 题目描述：
#   输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
#
# 解题思路：
#   1.利用栈先入后出的特性完成
#   2.顺序存入列表然后进行翻转（或直接用list的insert函数）
#   3.第三是利用递归。
#
# 成功方案：


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        while (cur != None):
            temp = cur.next  # 保存一下 cur的下一个节点，因为接下来要改变cur->next
            cur.next = pre  # 反转
            # 更新pre、cur指针
            pre = cur
            cur = temp
        return pre

#   1.顺序存入列表，然后翻转
def printListFromTailToHead(self, listNode):
    # write code here
    list = []
    if listNode == None:
        return list
    while listNode:
        list.append(listNode.val)
        listNode = listNode.next
    return list[::-1]  # 注意不能用list.reverse()替换list[::-1]   因为list.reverse()没有返回值


# 2.使用list的insert(),直接在首部插入
def printListFromTailToHead(self, listNode):
    # write code here
    l = []
    head = listNode
    while head:
        l.insert(0, head.val)
        head = head.next
    return l

#
# 注意事项：
# 不能用list.reverse()
# 替换list[::-1]
# 因为list.reverse()
# 没有返回值。
