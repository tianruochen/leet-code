# 题目描述：
#   用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
#
# 解题思路：
#   stack1 仅用于push
#   stack2 仅用于pop，如果stack2没有数据可以pop，则将stack1的数据全部pop出来存入stack2
#
# 成功方案：
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        # return xx
        if self.stack2 == []:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        return self.stack2.pop()
