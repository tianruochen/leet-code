# 题目描述：
# 请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
#
# 解题思路：
#    1、直接将字符串转换为列表逐个遍历替换（注意：不能直接对字符串进行修改），然后重新将列表转回字符串（方案2）
#    2、先遍历找到多少个空格，然后开辟数组填充（方案3）
#    3、思考：在当前字符串替换，怎么替换才更有效率
#       从前往后替换，后面的字符要不断往后移动，要多次移动，所以效率低下
#       从后往前，先计算需要多少空间，然后从后往前移动，则每个字符只为移动一次，这样效率更高一点。
#
# 成功方案：
#    1.
def replaceSpace(self, s):
    # write code he
    return s.replace(' ', '%20')


# 2.
def replaceSpace(self, s):
    # write code here
    s = list(s)
    count = len(s)
    for i in range(0, count):
        if s[i] == ' ':
            s[i] = '%20'
    return ''.join(s)


# 3.
def replaceSpace(s):
    # write code here
    s_len = len(s)
    space_count = 0
    for i in s:
        if i == ' ':
            space_count += 1
    s_len += 2 * space_count
    new_array = [' '] * s_len
    j = 0
    for i in range(len(s)):
        if s[i] == ' ':
            new_array[j] = '%'
            new_array[j + 1] = '2'
            new_array[j + 2] = '0'
            j += 3
        else:
            new_array[j] = s[i]
            j += 1
    return ''.join(new_array)


# 注意事项：1.
# 不能想访问数组一样直接对字符串元素进行修改
# 2.‘’不等于‘ ’！
