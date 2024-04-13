#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :4.zuida.py
# @Time     :2022/12/9 下午3:47
# @Author   :Chang Qing


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return None

        locMax = locMin = glbMax = nums[0]
        for n in nums[1:]:
            locMax, locMin = max(locMax * n, locMin * n, n), min(locMax * n, locMin * n, n)
            glbMax = max(locMax, glbMax)

        return glbMax
