# 代码实现：
# 每次经过一轮冒泡将最大值放到未排序队列的末尾
def bubble_sort(items):
    for i in range(len(items) - 1):
        flag = False
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                flag = True
        if not flag:
            break
    return items
