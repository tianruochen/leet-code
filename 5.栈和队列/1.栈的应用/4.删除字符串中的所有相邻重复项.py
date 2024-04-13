#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :4.删除字符串中的所有相邻重复项.py
# @Time     :2022/2/15 下午3:25
# @Author   :Chang Qing
 
"""
leetcode 1047
给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
在 S 上反复执行重复项删除操作，直到无法继续删除。
在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

示例：

输入："abbaca"
输出："ca"
解释：例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。
"""

# 方法一，使用栈，推荐！
class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = list()
        for item in s:
            if res and res[-1] == item:
                res.pop()
            else:
                res.append(item)
        return "".join(res)  # 字符串拼接


# 方法二，使用双指针模拟栈，如果不让用栈可以作为备选方法。
class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = list(s)
        slow = fast = 0
        length = len(res)

        while fast < length:
            # 如果一样直接换，不一样会把后面的填在slow的位置
            res[slow] = res[fast]

            # 如果发现和前一个一样，就退一格指针
            if slow > 0 and res[slow] == res[slow - 1]:
                slow -= 1
            else:
                slow += 1
            fast += 1

        return ''.join(res[0: slow])