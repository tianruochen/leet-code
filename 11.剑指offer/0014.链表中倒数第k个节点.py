# 题目描述
#   输入一个链表，输出该链表中倒数第k个结点。
#
# 解题思路：
#   1.最直接的方法：遍历链表统计个数num，倒数第k个，即正数第num-k+1个，再次遍历即可
#   2.使用列表，将遍历的元素放入列表a中，最后访问a[-k]即可
#   3.两个指针都指向头结点：
#         p指针先跑，并且记录节点数，当p指针跑了k-1个节点后，pre指针开始跑，
#         当p指针跑到最后时，pre所指指针就是倒数第k个节点
#
# 成功方案：

def FindKthToTail(self, head, k):
    # write code here
    num = 0
    pre = head
    while pre:
        num += 1
        pre = pre.next
    if num < k:
        return None
    pre = head
    for i in range(num - k):
        pre = pre.next
    return pre


# 2.


def FindKthToTail(self, head, k):
    # write code here
    l = []
    while head != None:
        l.append(head)
        head = head.next
    if k > len(l) or k < 1:
        return
    return l[-k]

#  1-- > 2
def FindKthToTail(self, head, k):
    if not head or not k:
        return None
    first = head
    second = head

    for i in range(k):
        if not first:
            return None
        first = first.next
    while first:
        first = first.next
        second = second.next
    return second
