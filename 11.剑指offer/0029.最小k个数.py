# 题目描述
#   输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
#
# 解题思路：
#   1.排序后输出即可
#   2.考虑到时间复杂度建议用堆排序 python中的heapq模块
#
# 成功方案：
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        l = len(tinput)
        if k > l or k <= 0:
            return []
        sortinput = sorted(tinput)
        return sortinput[:k]


import heapq


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if not tinput or not k or k > len(tinput):
            return []
        # 创建堆
        heapq.heapify(tinput)
        return [heapq.heappop(tinput) for _ in range(k)]
