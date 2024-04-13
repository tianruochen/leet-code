# 问题描述：
#   给定一个无重复元素的数组A[0…N-1]，求找到一个该数组的局部最大值。规定：在数组边界外的值无穷小。即：A[0]＞A[-1]，A[N-1] ＞A[N]。
# 显然，遍历一遍可以找到全局最大值，而全局最大值显然是局部最大值。
# 可否有更快的办法？
#
# 算法描述：
#   使用索引left、right分别指向数组首尾。
#   求中点 mid = ( left + right ) / 2
#   A[mid]＞A[mid+1]，丢弃后半段：right=mid
#   A[mid+1]＞A[mid]，丢弃前半段：left=mid+1
#   递归直至left==right
#   时间复杂度为O(logN)。
# 代码实现：
def local_maximum(li):
    if li is None:
        return
    left = 0
    right = len(li) - 1
    while left < right:
        mid = int((left + right) / 2)
        if li[mid] > li[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return li[left]


if __name__ == '__main__':
    li = [1, 5, 2, 3, 4, 0]
    result = local_maximum(li)
    print(result)
