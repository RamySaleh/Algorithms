from typing import List

matrix = [[1,2,3], [4,5,6], [7,8,9]]

def findDiagonalOrder(matrix: List[List[int]]) -> List[int]:
    if not matrix:
        return matrix
    i, j = 0, 0
    res = []
    up = True
    num_items = range(len(matrix) * len(matrix[0]))
    for idx in num_items:
        res.append(matrix[i][j])
        if up:
            if i == 0 and j == len(matrix[0]) - 1:
                i += 1
                up = not up
            elif i == 0:
                j += 1
                up = not up
            elif j == len(matrix[0]) - 1:
                i += 1
                up = not up
            else:
                i -= 1
                j += 1
        else:
            if j == 0 and i == len(matrix) - 1:
                j += 1
                up = not up
            elif j == 0:
                i += 1
                up = not up
            elif i == len(matrix) - 1:
                j += 1
                up = not up
            else:
                i += 1
                j -= 1

    return res

res = findDiagonalOrder(matrix)
print(res)