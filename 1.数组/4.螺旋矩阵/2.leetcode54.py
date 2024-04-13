#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :2.leetcode54.py
# @Time     :2022/2/10 下午9:52
# @Author   :Chang Qing

"""
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
输入:
[
[ 1, 2, 3 ],
[ 4, 5, 6 ],
[ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
https://blog.csdn.net/bulo1025/article/details/89289580
https://leetcode.cn/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/solution/shun-shi-zhen-da-yin-ju-zhen-by-leetcode-solution/

"""


#
#
# class Solution(object):
#     def spiralOrder(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: List[int]
#         """
#         result = []
#         if not matrix:
#             return []
#         row, col = len(matrix), len(matrix[0])
#         x1, x2, y1, y2 = 0, col - 1, 0, row - 1
#         while x1 <= x2 and y1 <= y2:              # 不再是统一的左闭右开
#             for i in range(x1, x2 + 1):
#                 result.append(matrix[y1][i])
#             for j in range(y1 + 1, y2 + 1):
#                 result.append(matrix[j][x2])
#             if x1 < x2 and y1 < y2:               # 如果只剩一行或一列的时候 没必要再打印一遍
#                 for i in range(x2 - 1, x1, -1):
#                     result.append(matrix[y2][i])
#                 for j in range(y2, y1, -1):
#                     result.append(matrix[j][x1])
#             x1 += 1
#             y1 += 1
#             x2 -= 1
#             y2 -= 1
#         return result
#
#
# class Solution(object):
#     def spiralOrder(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: List[int]
#         """
#
#         import math
#         if matrix == []:
#             return matrix
#         list1 = []
#         wide = len(matrix[0])
#         high = len(matrix)
#         rounds = (min(wide, high) + 1) // 2
#         for i in range(rounds):  # 轮次逐层计算
#             for j in range(4):  # 表示4个边，我们顺时针计算
#                 if j == 0:  # 表示上边
#                     list1 = list1 + [matrix[i][z] for z in range(i, wide - i)]
#                 elif j == 1:  # 表示右边
#                     list1 = list1 + [matrix[z][wide - i - 1] for z in range(i + 1, high - i)]
#                 elif j == 2 and high - i - 1 != i:  # 下方
#                     list1 = list1 + [matrix[high - i - 1][z] for z in range(wide - i - 2, i - 1, -1)]
#                 elif j == 3 and wide - i - 1 != i:  # 左边
#                     list1 = list1 + [matrix[z][i] for z in range(high - i - 2, i, -1)]
#         return list1
# #

class Solution(object):
    def spiralOrder(self, matrix):
        res = []
        rows = len(matrix)
        cols = len(matrix[0])
        left, up, right, down = 0, 0, cols - 1, rows - 1
        while left < right and up < down:             # 一致性， 左闭右开
            for x in range(left, right):
                res.append(matrix[up][x])
            for y in range(up, down):
                res.append(matrix[y][right])
            for x in range(right, left, -1):
                res.append(matrix[down][x])
            for y in range(down, up, -1):
                res.append(matrix[y][left])

            left += 1
            up += 1
            right -= 1
            down -= 1
        if up == down:
            for x in range(left, right+1):
                res.append(matrix[up][x])
        else:
            for y in range(up, down+1):
                res.append(matrix[y][left])
        print(res)


if __name__ == '__main__':
    a = [
        [1, 2, 3, 4],
        [4, 5, 6, 5],
        [7, 8, 9, 6]
    ]
    # a = [
    #     [1, 2],
    #     [4, 5]
    # ]
    res = Solution().spiralOrder(a)
    print(res)
