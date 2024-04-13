# 题目描述:
#   给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
#
# 解题思路：
#   1.直接用python内置函数pow()
#   2.循环解决（注意考察指数的类型，分段考虑）
#
# 成功方案：

def Power(self, base, exponent):
    # write code here
    return pow(base, exponent)


def Power(self, base, exponent):
    # write code here
    flag = 0
    if base == 0:
        return False
    if exponent == 0:
        return 1
    if exponent < 0:
        flag = 1
    result = 1
    for i in range(abs(exponent)):
        result *= base
    if flag == 1:
        result = 1 / result
    return result
