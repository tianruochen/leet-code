#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :2.摆动序列.py
# @Time     :2022/3/4 上午11:39
# @Author   :Chang Qing
 
"""
leetcode 376

如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。第一个差（如果存在的话）可能是正数或负数。少于两个元素的序列也是摆动序列。

例如， [1,7,4,9,2,5] 是一个摆动序列，因为差值 (6,-3,5,-7,3) 是正负交替出现的。相反, [1,4,7,2,5] 和 [1,7,4,5,5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。

给定一个整数序列，返回作为摆动序列的最长子序列的长度。 通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。

示例 1:

输入: [1,7,4,9,2,5]
输出: 6
解释: 整个序列均为摆动序列。
示例 2:

输入: [1,17,5,10,13,15,10,5,16,8]
输出: 7
解释: 这个序列包含几个长度为 7 摆动序列，其中一个可为[1,17,10,13,10,16,8]。
示例 3:

输入: [1,2,3,4,5,6,7,8,9]
输出: 2

细节：
本题代码实现中，还有一些技巧，例如统计峰值的时候，数组最左面和最右面是最不好统计的。

例如序列[2,5]，它的峰值数量是2，如果靠统计差值来计算峰值个数就需要考虑数组最左面和最右面的特殊情况。

所以可以针对序列[2,5]，可以假设为[2,2,5]，这样它就有坡度了即preDiff = 0，

https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0376.%E6%91%86%E5%8A%A8%E5%BA%8F%E5%88%97.md
"""


class Solution:
    def wiggleMaxLength(self, nums):
        # res记录峰值个数，默认序列最右边有一个峰值
        preC,curC,res = 0,0,1  #题目里nums长度大于等于1，当长度为1时，其实到不了for循环里去，所以不用考虑nums长度
        for i in range(len(nums) - 1):
            curC = nums[i + 1] - nums[i]
            if curC * preC <= 0 and curC !=0:  #差值为0时，不算摆动
                res += 1
                preC = curC  #如果当前差值和上一个差值为一正一负时，才需要用当前差值替代上一个差值
        return res

    def wiggleMaxLength2(self, nums):
        """
        我们只需要统计该序列中「峰」与「谷」的数量即可（注意序列两端的数也是「峰」或「谷」），
        但需要注意处理相邻的相同元素。

        在实际代码中，我们记录当前序列的上升下降趋势。每次加入一个新元素时，用新的上升下降趋势与之前对比，
        如果出现了「峰」或「谷」，答案加一，并更新当前序列的上升下降趋势。

        :param nums:
        :return:
        """
        n = len(nums)
        if n < 2:
            return n

        prevdiff = nums[1] - nums[0]
        ret = (2 if prevdiff != 0 else 1)
        for i in range(2, n):
            diff = nums[i] - nums[i - 1]
            # 为什么 不能是 <0 而一定要是 <=0
            # 原因 [3,3,3,2,5]
            if (diff * prevdiff <= 0) and diff != 0: #差值为0时，不算摆动
                ret += 1
                prevdiff = diff      # 将prevdiff视为趋势 向上或向下

        return ret




if __name__ == '__main__':
    nums = [1,2,2,3,4,4,5]
    res = Solution().wiggleMaxLength2(nums)
    print(res)