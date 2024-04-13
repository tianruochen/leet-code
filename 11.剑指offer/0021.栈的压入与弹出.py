# 题目描述
#   输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。
# 例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
# （注意：这两个序列的长度是相等的）
#
# 解题思路：
#   引入一个新的栈，根据入栈顺序入栈，入栈后判断栈顶元素是否和出站顺序中的元素相等，相等则都出站，最后判断新的栈中元素为0则返回true，否则返回false
#
# 成功方案：
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or len(pushV) != len(popV):
            return False
        stack = []
        for i in pushV:
            stack.append(i)
            while len(stack) and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        if len(stack):
            return False
        return True
        
    # 注意事项：
    #    popV.pop()删除尾部元素
    #    popV.pop(0)删除首部元素
