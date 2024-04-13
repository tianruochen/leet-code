# 题目描述
#   数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
#
# 解题思路：
#   1.直接使用 collections.Counter()统计数组中所有的元素及其次数。返回一个字典。
#   2.对数组排序，如果存在这样的数那么其一定是排序后数组中间的数。然后统计该数的数量。
#
# 成功方案：
import collections


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        tmp = collections.Counter(numbers)
        x = len(numbers) / 2
        for k, v in tmp.items():
            if v > x:
                return k
        return 0


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        num = sorted(numbers)
        x = len(numbers) / 2
        count = 0
        for i in numbers:
            if i == num[x]:
                count += 1
        if count > x:
            return num[x]
        return 0
