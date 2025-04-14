def binerySeacTwoD( matrix, target):
    m = len(matrix)
    n = len(matrix[0])

    if m == 0:
        return False
    left = 0
    right = m * n - 1

    while left <= right:
        mid = left + (right - left) // 2
        mid_ele = matrix[mid // n][mid % n]

        if mid_ele == target:
            return True
        elif mid_ele < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# Driver code
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [21, 30, 60, 64]]
target = 30
result = binerySeacTwoD(matrix, target)
print(result)
