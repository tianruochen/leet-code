# 题目描述：
# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
#
# 解题思路：
#     利用二维数组由上到下，由左到右递增的规律，
#     那么选取右上角或者左下角的元素a[row][col]与target进行比较，
#     当target小于元素a[row][col]时，那么target必定在元素a所在行的左边,
#     即col--；
#     当target大于元素a[row][col]时，那么target必定在元素a所在列的下边,
#     即row++；
#
# 成功方案：
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        row = len(array)
        col = len(array[0])
        i = 0
        j = col-1
        while i<=row-1 and j>=0:
            base = array[i][j]
            if base == target:
                return True
            elif base < target:
                i +=1
            else:
                j -=1 
        return False

# 注意事项： python中不存在 i++这种表达。
#           二维数组的行数：row = len(array)
#           二维数组的列数：col = len(array[0])
