# 题目描述
#   统计一个数字在排序数组中出现的次数。
  
# 解题思路：
#   1.一个头标，一个尾标，
#     一个从前搜索，一个从尾搜索，遇到与该数字相等的位置 停止
#     两个标志相减即可（如果尾标<头标 返回0）
#
# 成功方案：

class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        return data.count(k)


# 3.推荐方案：整体用二分法，找到头和尾。
#
#         因为data中都是整数，所以可以稍微变一下，不是搜索k的两个位置，而是搜索k-0.5和k+0.5
#
#         这两个数应该插入的位置，然后相减即可,不需要加1。
#
#         总结：折半查找插入位置  while 循环 low<=high  raturn low ----low的位置就是应该插入的位置。
        
class Solution:
    def biSearch(self,data, k):
        low = 0
        high = len(data) - 1
        while low <= high:
            mid = (low + high) // 2
            if data[mid] > k:
                high = mid - 1
            elif data[mid] < k:
                low = mid + 1
        return low

    def GetNumberOfK(self,data, k):
        # write code here
        if not data: return 0
        return self.biSearch(data, k+0.5) - self.biSearch(data, k-0.5)
