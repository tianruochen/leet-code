# 思路：
#     快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为较小和较大的2个子序列，然后递归地排序两个子序列。
#
#     步骤为：
#         挑选基准值：从数列中挑出一个元素，称为"基准"（pivot）;
#         分割：重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（与基准值相等的数可以到任何一边）。
#      在这个分割结束之后，对基准值的排序就已经完成;
#         递归排序子序列：递归地将小于基准值元素的子序列和大于基准值元素的子序列排序。
#
#  代码实现：
#
#  1.超简洁版本（容易理解记忆）
 def quickSort(array):
    if len(array) < 2:  # 基线条件（停止递归的条件）
        return array
    else:  # 递归条件
        baseValue = array[0]  # 选择基准值
        # 由所有小于基准值的元素组成的子数组
        less = [m for m in array[1:] if m < baseValue]
        # 包括基准在内的同时和基准相等的元素，在上一个版本的百科当中，并没有考虑相等元素
        equal = [w for w in array if w == baseValue]
        # 由所有大于基准值的元素组成的子数组
        greater = [n for n in array[1:] if n > baseValue]
    return quickSort(less) + equal + quickSort(greater)
# 示例：
array = [2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12]
print(quickSort(array))


2.比较常见的一个版本 
def quick_sort(alist, start, end):
    if start >= end:
        # 退出递归
        return
    pivot = alist[start]
    right = end
    left = start

    # 控制right -= 1不满足条件交换
    while left < right:
        while left < right and alist[right] >= pivot:
            right -= 1
        if left<right:
            alist[left] = alist[right]
        # 控制 left += 1 , 不满足条件交换
        while left < right and alist[left] <= pivot:
            left += 1
        if left < right:
            alist[right] = alist[left]

    # 退出循环 left = right
    # left 或者 right 对应的位置 赋值为基准值
    alist[left] = pivot

    # 递归自己调用自己
    print(alist)
    quick_sort(alist, start, left - 1)  # 对左边排序
    quick_sort(alist, left + 1, end)  # 对右边排序


if __name__ == '__main__':
    li = [6, 7, 1, 3, 4, 1, 8]
    quick_sort(li, 0, len(li) - 1)
    print(li)
