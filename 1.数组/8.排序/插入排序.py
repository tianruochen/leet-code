#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :归并排序.py
# @Time     :2022/11/9 下午3:07
# @Author   :Chang Qing
 
"""
排序原理：
  以从小到大排序为例，元素0为第一个元素，插入排序是从元素1开始，尽可能插到前面。插入时分插入位置和试探位置，
  元素i的初始插入位置为i，试探位置为i-1，在插入元素i时，依次与i-1,i-2······元素比较，如果被试探位置的元素比插入元素大，
  那么被试探元素后移一位，元素i插入位置前移1位，直到被试探元素小于插入元素或者插入元素位于第一位。
"""

def insertSort(arr):
    length = len(arr)
    for i in range(1,length):
        x = arr[i]
        for j in range(i-1,-1,-1):
            # j为当前位置，试探j-1位置
            if x < arr[j]:
                arr[j+1] = arr[j]
            else:
                # 位置确定为j+1
                break
        arr[j+1] = x

def printArr(arr):
    for item in arr:
        print(item)
arr = [4, 7 ,8 ,2 ,3 ,5]
insertSort(arr)
printArr(arr)