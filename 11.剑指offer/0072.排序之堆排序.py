# 堆节点的访问
# 在这里我们借用wiki的定义来说明：
# 通常堆是通过一维数组来实现的。在阵列起始位置为0的情况中
# (1)父节点i的左子节点在位置(2*i+1);
# (2)父节点i的右子节点在位置(2*i+2);
# (3)子节点i的父节点在位置floor((i-1)/2);
#
# 堆操作
# 堆可以分为大根堆和小根堆，这里用最大堆的情况来定义操作:
# (1)最大堆调整(MAX_Heapify):将堆的末端子节点作调整，使得子节点永远小于父节点。这是核心步骤，在建堆和堆排序都会用到。比较i的根节点和与其所对应i的孩子节点的值。当i根节点的值比左孩子节点的值要小的时候，就把i根节点和左孩子节点所对应的值交换，当i根节点的值比右孩子的节点所对应的值要小的时候，就把i根节点和右孩子节点所对应的值交换。然后再调用堆调整这个过程，可见这是一个递归的过程。
# (2)建立最大堆(Build_Max_Heap):将堆所有数据重新排序。建堆的过程其实就是不断做最大堆调整的过程，从下标len//2-1出开始调整，一直比到下标为0的节点。
# (3)堆排序(HeapSort):移除位在第一个数据的根节点，并做最大堆调整的递归运算。堆排序是利用建堆和堆调整来进行的。首先先建堆，然后将堆的根节点选出与最后一个节点进行交换，然后将前面len-1个节点继续做堆调整的过程。直到将所有的节点取出，对于n个数我们只需要做n-1次操作。
#
#
#
# 代码实现：
import random

#完成一次节点root到最终位置heapsize的调整,
#从指定的起点到终点的序列 进行一次堆调整
def MAX_Heapify(heap,start,end):#在堆中做结构调整使得父节点的值大于子节点

    left = 2*start + 1               #因为我们的下标是从0开始的，所以左孩子的坐标为 2*root+1
    right = left + 1
    larger = start
    if left < end and heap[larger] < heap[left]:
        larger = left
    if right < end and heap[larger] < heap[right]:
        larger = right
    if larger != start:#如果做了堆调整则larger的值等于左节点或者右节点的，这个时候做对调值操作
        heap[larger],heap[start] = heap[start],heap[larger]
        MAX_Heapify(heap, larger, end)

def Build_MAX_Heap(heap):#构造一个堆，将堆中所有数据重新排序
    HeapSize = len(heap)#将堆的长度当独拿出来方便
    for i in range(HeapSize//2-1,-1,-1):#从后往前出数   #注意在树的定义中下标是从1开始的，而我们的实现中下标是从0开始的
        MAX_Heapify(heap,i,HeapSize)

def HeapSort(heap):#将根节点取出与最后一位做对调，对前面len-1个节点继续进行对调整过程。
    Build_MAX_Heap(heap)
    for i in range(len(heap)-1,-1,-1):
        heap[0],heap[i] = heap[i],heap[0]
        MAX_Heapify(heap, 0,i)
    return heap

if __name__ == '__main__':
    a = [30,50,57,77,62,78,94,80,84]
    print(a)
    HeapSort(a)
    print(a)
    b = [random.randint(1,100) for i in range(100)]
    print(b)
    HeapSort(b)
    print(b)
