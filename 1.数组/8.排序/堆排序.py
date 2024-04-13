#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :堆排序.py
# @Time     :2022/11/9 下午4:52
# @Author   :Chang Qing


def MAX_Heapify(heap, start, end):  # 在堆中做结构调整使得父节点的值大于子节点

    left = 2 * start + 1  # 因为我们的下标是从0开始的，所以左孩子的坐标为 2*root+1
    right = left + 1
    larger = start
    if left < end and heap[larger] < heap[left]:
        larger = left
    if right < end and heap[larger] < heap[right]:
        larger = right
    if larger != start:  # 如果做了堆调整则larger的值等于左节点或者右节点的，这个时候做对调值操作
        heap[larger], heap[start] = heap[start], heap[larger]
        MAX_Heapify(heap, larger, end)



def Build_MAX_Heap(heap):  # 构造一个堆，将堆中所有数据重新排序
    HeapSize = len(heap)  # 将堆的长度当独拿出来方便
    for i in range(HeapSize // 2 - 1, -1, -1):  # 从后往前出数   #注意在树的定义中下标是从1开始的，而我们的实现中下标是从0开始的
        MAX_Heapify(heap, i, HeapSize)


def HeapSort(heap):  # 将根节点取出与最后一位做对调，对前面len-1个节点继续进行对调整过程。
    Build_MAX_Heap(heap)
    for i in range(len(heap) - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        MAX_Heapify(heap, 0, i)
    return heap


if __name__ == '__main__':
    a = [30, 50, 57, 77, 62, 78, 94, 80, 84]
    print(a)
    print(HeapSort(a))
