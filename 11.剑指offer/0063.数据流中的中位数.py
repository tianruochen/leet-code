# 题目描述
#     如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，
# 那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
#
# 成功方案：
class Solution:
    def __init__(self):
        self.res = []
    def Insert(self, num):
        # write code here
        
        self.res.append(num)
        self.res.sort()
    def GetMedian(self,data):
        # write code here
        l = len(self.res)
        if l%2==0:
            return (self.res[l//2]+self.res[l//2-1])/2.0
        else:
            return self.res[l//2]
        
