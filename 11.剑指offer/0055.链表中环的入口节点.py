题目描述
  给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
  
解题思路：
  #遍历链表，环的存在，遍历遇见的第一个重复的即为入口节点
  
成功方案：
  def EntryNodeOfLoop(self, pHead):
        # write code here
        
        tempList = []
        p = pHead
        while p:
            if p in tempList:
                return p
            else:
                tempList.append(p)
            p = p.next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # 如果相遇
            if slow == fast:
                p = head
                q = slow
                while p!=q:
                    p = p.next
                    q = q.next
                #你也可以return q
                return p

        return None