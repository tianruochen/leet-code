# 题目描述
#     请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
# 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
#
# 解题思路：
'''

当模式中的第二个字符不是“*”时：
        1、如果字符串第一个字符和模式中的第一个字符相匹配，那么字符串和模式都后移一个字符，然后匹配剩余的。
        2、如果 字符串第一个字符和模式中的第一个字符相不匹配，直接返回false。

而当模式中的第二个字符是“*”时：
        如果字符串第一个字符跟模式第一个字符不匹配，则模式后移2个字符，继续匹配。如果字符串第一个字符跟模式第一个字符匹配，可以有3种匹配方式：
        1、模式后移2字符，相当于x*被忽略；
        2、字符串后移1字符，模式后移2字符；
        3、字符串后移1字符，模式不变，即继续匹配字符下一位，因为*可以匹配多位；
'''

成功方案：
  class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # 如果s与pattern都为空，则True
        if len(s) == 0 and len(pattern) == 0:
            return True
        # 如果s不为空，而pattern为空，则False
        elif len(s) != 0 and len(pattern) == 0:
            return False
        # 如果s为空，而pattern不为空，则需要判断
        elif len(s) == 0 and len(pattern) != 0:
            # pattern中的第二个字符为*，则pattern后移两位继续比较
            if len(pattern) > 1 and pattern[1] == '*':
                return self.match(s, pattern[2:])
            else:
                return False
        # s与pattern都不为空的情况
        else:
            # pattern的第二个字符为*的情况
            if len(pattern) > 1 and pattern[1] == '*':
                # s与pattern的第一个元素不同，则s不变，pattern后移两位，相当于pattern前两位当成空
                if s[0] != pattern[0] and pattern[0] != '.':
                    return self.match(s, pattern[2:])
                else:
                    # 如果s[0]与pattern[0]相同，且pattern[1]为*，这个时候有三种情况
                    # pattern后移2个，s不变；相当于把pattern前两位当成空，匹配后面的
                    # pattern后移2个，s后移1个；相当于pattern前两位与s[0]匹配
                    # pattern不变，s后移1个；相当于pattern前两位，与s中的多位进行匹配，因为*可以匹配多位
                    return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)
            # pattern第二个字符不为*的情况
            else:
                if s[0] == pattern[0] or pattern[0] == '.':
                    return self.match(s[1:], pattern[1:])
                else:
                    return False
