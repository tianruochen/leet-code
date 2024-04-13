# 题目描述
#   输入两个链表，找出它们的第一个公共结点。
#
# 解题思路：
#   1.循环第一个链表，保存其所有的值到列表中，然后迭代第二个链表元素，判断其值是否在列表中
#   2.倒序看，p1和p2两个链表的第一个公共结点到尾结点的长度一定相同。因此我们先对齐两个链表，再一起往后走找到第一个公共结点即可。
#
#         找出两个链表长度，n1和n2，长的链表先走n1-n2步。
#         一起往后走，找到第一个公共结点。
#
# 成功方案：
def FindFirstCommonNode(self, pHead1, pHead2):
    # write code here
    p1 = pHead1
    p2 = pHead2
    n_p1 = 0
    n_p2 = 0
    while p1:
        p1 = p1.next
        n_p1 += 1
    while p2:
        p2 = p2.next
        n_p2 += 1
    if n_p1 < n_p2:
        pHead1, pHead2 = pHead2, pHead1
    for _ in range(n_p1 - n_p2):
        pHead1 = pHead1.next
    while pHead1:
        if pHead1 == pHead2:
            return pHead1
        else:
            pHead1 = pHead1.next
            pHead2 = pHead2.next
    return None


def FindFirstCommonNode(self, pHead1, pHead2):
    # write code here
    list1 = []
    list2 = []
    node1 = pHead1
    node2 = pHead2
    while node1:
        list1.append(node1)
        node1 = node1.next
    while node2:
        if node2 in list1:
            return node2
        else:
            node2 = node2.next


3.


def FindFirstCommonNode(self, pHead1, pHead2):
    # write code here

    pre1 = pHead1
    pre2 = pHead2
    while pre1:
        while pre2:
            if pre2.val == pre1.val:
                return pre2
            pre2 = pre2.next
        pre1 = pre1.next
        pre2 = pHead2
    return None
