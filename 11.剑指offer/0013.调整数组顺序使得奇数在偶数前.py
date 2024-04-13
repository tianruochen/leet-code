# 题目描述
#   输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
# 所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
#
# 解题思路：
#   1.最直接的思路：找出所有的奇数，偶数，将其拼接在一起
#   2.使用deque（双端队列）的appendleft函数。奇数要从后往前循环然后左插（这是为了保证最终的奇数顺序不变），偶数从前往后循环然后append
#
# 成功方案：
def reOrderArray(self, array):
    # write code here
    jishu = [i for i in array if i % 2 == 1]
    oushu = [i for i in array if i % 2 == 0]
    result = []
    result.extend(jishu)
    result.extend(oushu)
    return result


from collections import deque


def reOrderArray(self, array):
    odd = deque()
    x = len(array)
    for i in range(x):
        if array[x - i - 1] % 2 != 0:
            odd.appendleft(array[x - i - 1])
        if array[i] % 2 == 0:
            odd.append(array[i])
    return list(odd)
