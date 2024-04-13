# 题目描述
#   输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
#
# 解题思路
#   两个链表逐个比较，小的插入新链表，最后谁有剩余，直接插入新链表即可（注意为了操作方便，可以先申请一个无效的节点当做头结点）
#
# 成功方案：
def Merge(self, pHead1, pHead2):
    # write code here

    # 申请一个无效节点作为头结点
    mergeHead = ListNode(90)
    p = mergeHead
    while pHead1 and pHead2:
        if pHead1.val >= pHead2.val:
            mergeHead.next = pHead2
            pHead2 = pHead2.next
        else:
            mergeHead.next = pHead1
            pHead1 = pHead1.next

        mergeHead = mergeHead.next
    if pHead1:
        mergeHead.next = pHead1
    elif pHead2:
        mergeHead.next = pHead2

    # 从第一个节点返回，头结点是无效的
    return p.next
