# 题目描述
#     输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
# 输出描述:
#     对应每个测试案例，输出两个数，小的先输出。
#
# 成功方案：
# -*- coding:utf-8 -*-

def FindNumbersWithSum(self, array, tsum):
    # write code here
    if not isinstance(array, list):
        return None
    for i in range(len(array)):
        if tsum - array[i] in array:
            return array[i], tsum - array[i]


def FindNumbersWithSum(self, array, tsum):
    ls = []
    if not isinstance(array, list):
        return ls
    for i, v in enumerate(array):
        for v1 in array[i + 1:]:
            if v + v1 == tsum:
                ls.append([v, v1])
    if ls:
        return ls[0]
    else:
        return ls


def FindNumbersWithSum(self, array, tsum):
    # write code here
    if not array: return []
    lp = 0
    rp = len(array) - 1

    while lp < rp:
        tmp = array[lp] + array[rp]
        if tmp > tsum:
            rp -= 1
        elif tmp < tsum:
            lp += 1
        elif tmp == tsum:
            return array[lp], array[rp]

    return []
