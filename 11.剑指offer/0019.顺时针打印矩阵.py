class Solution(object):
    def spiralOrder(self, matrix):
        res = []
        rows = len(matrix)
        cols = len(matrix[0])
        left, up, right, down = 0, 0, cols - 1, rows - 1
        while left < right and up < down:             # 一致性， 左闭右开
            for x in range(left, right):
                res.append(matrix[up][x])
            for y in range(up, down):
                res.append(matrix[y][right])
            for x in range(right, left, -1):
                res.append(matrix[down][x])
            for y in range(down, up, -1):
                res.append(matrix[y][left])

            left += 1
            up += 1
            right -= 1
            down -= 1
        if up == down:
            for x in range(left, right+1):
                res.append(matrix[up][x])
        else:
            for y in range(up, down+1):
                res.append(matrix[y][left])
        print(res)


if __name__ == '__main__':
    a = [
        [1, 2, 3, 4],
        [4, 5, 6, 5],
        [7, 8, 9, 6]
    ]
    # a = [
    #     [1, 2],
    #     [4, 5]
    # ]
    res = Solution().spiralOrder(a)
    print(res)
