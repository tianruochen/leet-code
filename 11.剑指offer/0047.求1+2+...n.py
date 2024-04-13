# 题目描述
#   求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
#
# 成功方案：
# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        return sum(range(n+1))
    
    # def __init__(self):
    #     self.sum = 0
    #
    #
    # def Sum_Solution(self, n):
    #     # write code here
    #     self.qiusum(n)
    #     return self.sum
    # def qiusum(self,n):
    #     self.sum += n
    #     n -= 1
    #     return n>0 and self.qiusum(n)

    def Sum_Solution(self, n):
        # 1. 在计算 a and b 时，如果 a 是 False，则根据与运算法则，整个结果必定为 False，因此返回 a；如果 a 是 True，则整个计算结果必定取决与 b，因此返回 b。
        # 2. 在计算 a or b 时，如果 a 是 True，则根据或运算法则，整个计算结果必定为 True，因此返回 a；如果 a 是 False，则整个计算结果必定取决于 b，因此返回 b。
        return n and n+self.Sum_Solution(n-1)
