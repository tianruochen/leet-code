# 题目描述
#   在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。
# 并将P对1000000007取模的结果输出。 即输出P%1000000007
#
# 超时方案：
class Solution:
    def InversePairs(self, data):
        # write code here
        l = len(data)
        count = 0
        for i in range(l - 1):
            for j in range(i+1, l):
                if data[i] > data[j]:
                    count += 1
        return count


# 2. 首先想到的是冒泡排序法，也就是两两比较，时间复杂度为（n^2），
# 这里对冒泡排序进行一定改进：某次比较过程中，如果没有两个元素交换位置，则说明已经排好序，退出循环。
def test(array):
    t = 0
    for i in range(len(array) - 1, 0, -1):
        flag = False
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                t += 1
                flag = True
        if not flag:
            break
    return t % (2 * (10 ** 5))


# 3.根据归并排序的原理，可得到时间复杂度为O(n*logn)的方法，也就是在归并排序法的基础上添加一行代码：cout=+len(left)-l

class Solution:
    def InversePairs(self, data):
        # 冒牌排序法，时间复杂度太高，时间复杂度为O（n^2）。采用归并排序的思想,时间复杂度为O（nlogn）
        global count
        count = 0

        def A(array):
            global count
            if len(array) <= 1:
                return array
            k = int(len(array) / 2)
            left = A(array[:k])
            right = A(array[k:])
            l = 0
            r = 0
            result = []
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    result.append(left[l])
                    l += 1
                else:
                    result.append(right[r])
                    r += 1
                    count += len(left) - l
            result += left[l:]
            result += right[r:]
            return result

        A(data)
        return count % 1000000007


# 4.最后网上还看到一个更加简洁（牛逼）的方法：
#
# 先将原序列排序，然后从排完序的数组中取出最小的，它在原数组中的位置表示有多少比它大的数在它前面，每取出一个在原数组中删除该元素，保证后面取出的元素在原数组中是最小的，这样其位置才能表示有多少比它大的数在它前面，即逆序对数。
class Solution:
    def InversePairs(self, data):
        count = 0
        copy = []
        for i in data:
            copy.append(i)
        copy.sort()
        for i in range(len(copy)):
            count += data.index(copy[i])
            data.remove(copy[i])
        return count % 1000000007


a = [1, 2, 3, 4, 5, 6, 7, 0]
Solution().InversePairs(a)

# 补充：归并排序：https://www.cnblogs.com/bianjing/p/10260264.html
