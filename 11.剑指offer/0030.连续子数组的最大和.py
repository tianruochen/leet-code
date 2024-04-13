# 题目描述
#   HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,
# 当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？
#   例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？
# (子向量的长度至少是1)
#
# 解题思路：
#       1./*
#            (1) 常规方法,时间复杂度O（n*n）
#            (2) 先从第一个元素开始向后累加，
#            (3)每次累加后与之前的和比较，保留最大值，
#            (4) 再从第二个元素开始向后累加，以此类推
#           */
#       2.
#           /*
#          （1） 最优方法，时间复杂度O（n）
#          （2） 和最大的子序列的第一个元素肯定是正数
#          （3） 因为元素有正有负，因此子序列的最大和一定大于0
#            */
#
#
# 成功方案：
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if len(array) <= 0:
            return
        tempsum = 0
        maxsum = -10000
        for i in array:
            tempsum += i
            if tempsum >= maxsum:
                maxsum = tempsum
            if tempsum < 0:
                tempsum = 0
        return maxsum


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if len(array) <= 0:
            return []
        temp_sum = 0
        list_sum = []
        for i in array:
            temp_sum = temp_sum + i
            list_sum.append(temp_sum)
            if temp_sum > 0:
                continue
            else:
                temp_sum = 0
        return max(list_sum)
