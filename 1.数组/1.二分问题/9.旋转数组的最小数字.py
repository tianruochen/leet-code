# 问题描述：
#   把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
#
# 解题思路：
#   说了一大堆，其实就是求一个数组的最小值。
#
# 成功方案
def minNumberInRotateArray(self, rotateArray):
    # write code here
    pre = -7e20
    for num in rotateArray:
        if num < pre:
            return num
        pre = num

    if len(rotateArray) == 0:
        return 0
    return rotateArray[0]


2.


def minNumberInRotateArray(self, rotateArray):
    return min(rotateArray[0])


3.


def minNumberInRotateArray(self, rotateArray):
    # write code here
    if len(rotateArray) == 0:
        return 0

    ret = rotateArray[0]
    if len(rotateArray) == 1:
        return ret

    for i in range(1, len(rotateArray)):
        now = rotateArray[i]
        if now < ret:
            ret = now
            break
    return ret

#
# 最佳方法：折半查找：
# 旋转之后的数组实际上可以划分成两个有序的子数组：前面子数组的大小都大于后面子数组中的元素
#
# 注意到实际上最小的元素就是两个子数组的分界线。
#
# 用索引left，right分别指向首尾元素，元素不重复。
# 若子数组是普通升序数组，则A[left] < A[right]。
# 若子数组是循环升序数组，前半段子数组的元素全都大于后半段子数组中的元素：A[left] > A[right]
# 计算中间位置
# mid = (low + high) / 2
# 显然，A[low…mid]与A[mid + 1…high]必有一个是循环升序数组，一个是普通升序数组。
# 若：A[mid] > A[high]，说明子数组A[mid + 1, mid + 2,…high]循环升序，更新low = mid + 1；
# 若：A[mid] < A[high] ，说明子数组A[mid + 1, mid + 2,…high]普通升序，更新high = mid


def find_min(li):
    low = 0
    high = len(li) - 1
    while low < high:
        mid = int((low + high) / 2)
        if li[mid] > li[high]:
            low = mid + 1
        else:
            high = mid
    return li[low]
