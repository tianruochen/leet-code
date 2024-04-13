# 题目描述
#   在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
#
# 解题思路：
#   #使用字符串的统计函数count：s.count(s[i])
#
# 成功方案
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        for i in range(len(s)):
            if s[i] not in s[:i] + s[i + 1:]:
                return i
        return -1


class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i
        return -1
