#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :3.字母异位词分组.py
# @Time     :2022/2/14 上午11:38
# @Author   :Chang Qing
 

"""
leetcode 49
字母异位词分组（LeetCode49）
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串
  输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
  输出: [ ["ate","eat","tea"], ["nat","tan"], ["bat"] ]

reference：
https://blog.csdn.net/weixin_41855010/article/details/106505984
"""
# 方法一
lst = ["eat", "tea", "tan", "ate", "nat", "bat"]
dct = {}
for i in lst:
	key = str(sorted(i))
	if key not in dct.keys():
		dct[key] = [i]
	else:
		dct[key].append(i)
res = [val for val in dct.values()]
print(res)


# 方法二 特征向量法
import collections
from collections import defaultdict
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
dct = defaultdict(list)
for s in strs:
	count = [0] * 26
	for i in s:
		count[(ord(i)-ord('a'))] += 1
	#注意key只能是不可变的数值
	key = tuple(count)
	dct[tuple(count)].append(s)
res = [val for val in dct.values()]
print(res)
