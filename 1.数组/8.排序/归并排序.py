#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :归并排序.py
# @Time     :2022/11/9 下午3:07
# @Author   :Chang Qing
 
"""
思路：首先归并排序使用了二分法，归根到底的思想还是分而治之。
      拿到一个长数组，将其不停的分为左边和右边两份，然后以此递归分下去。然后再将她们按照两个有序数组的样子合并起来。

      两个有序数组排序的方法则非常简单，同时对两个数组的第一个位置进行比大小，将小的放入一个空数组，然后被放入空数
组的那个位置的指针往后 移一个，然后继续和另外一个数组的上一个位置进行比较，以此类推。到最后任何一个数组先出栈完，就将
另外i一个数组里的所有元素追加到新数组后面。由于递归拆分的时间复杂度是logN 然而，进行两个有序数组排序的方法复杂度是N该
算法的时间复杂度是N*logN 所以是NlogN。
"""

def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    return c


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists)//2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)


if __name__ == '__main__':
    a = [14, 2, 34, 43, 21, 19]
    print (merge_sort(a))