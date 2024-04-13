# 题目描述
#   输入一个链表，反转链表后，输出新链表的表头。
#
# 解题思路：遍历链表，逐个头插
#
# 成功方案：
def ReverseList(self, pHead):
        # write code here
    
        if not pHead or not pHead.next:
            return pHead
          
        last = None
          
        while pHead:
            tmp = pHead.next
            pHead.next = last
            last = pHead
            pHead = tmp
        return last
          
