# 题目描述：
#   输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
#
# 解题思路：
#   移位运算会自动将整数转为2进制，复数会转换为补码形式，通过>> 并与1进行&运算 可以不断的获得移位后最后一位是否为1
#
# 成功方案：
def NumberOf1(self, n):
    # write code here
    return sum([(n >> i & 1) for i in range(0, 32)])


def NumberOf1(n):
    ret = 0
    while n:
        ret += 1
        n = n & n - 1
    return ret
