# 题目描述
#   大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0。n<=39
#
# 解题思路：用循环，不要用递归（递归时间复杂度高）
#
# 成功案列
def Fibonacci(self, n):
    # write code here
    a = [0, 1, 1]
    if n < 3:
        return a[n]
    for i in range(3, n + 1):
        a.append(a[i - 1] + a[i - 2])
    return a[n]


def Fibonacci(self, n=39):
    # write code here
    f0, f1 = 0, 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    for i in range(2, n + 1):
        a = f0 + f1
        f0 = f1
        f1 = a
    return a


def Fibonacci(self, n):  # 递归的写法
    if n == 0:
        return 0
    if n == 1:
        return 1
    return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)
