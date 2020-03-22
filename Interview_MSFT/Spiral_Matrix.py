# https://leetcode.com/problems/spiral-matrix/
from typing import List

from Helpers import helper as hlp
from Helpers import test_class
import random


class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return res

        counter = r = c = 0
        h = len(matrix)
        w = len(matrix[0])
        v = [[False for _ in range(w)] for _ in range(h)]

        while self.notTheEnd(r, c, v):
            if 0 <= r < h and 0 <= c < w and not v[r][c]:
                res.append(matrix[r][c])
                v[r][c] = True

            newStep = self.getNextStep(r, c, counter)

            # is next step valid
            if 0 <= newStep[0] < h and 0 <= newStep[1] < w and not v[newStep[0]][newStep[1]]:
                r, c = newStep
            else:  # Change direction
                counter += 1

        return res

    def getNextStep(self, r, c, counter):
        if counter % 4 == 0:
            c += 1
        elif counter % 4 == 1:
            r += 1
        elif counter % 4 == 2:
            c -= 1
        else:
            r -= 1
        return r, c

    def notTheEnd(self, r, c, v):
        for row in v:
            if False in row:
                return True
        return False

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return res

        dir = 0
        l, r = 0, len(matrix[0])
        t, b = 0, len(matrix)

        while b >= t and r >= l:
            if dir == 0:
                for col in range(l, r):
                    res.append(matrix[t][col])
                    dir = 1
                t += 1
            elif dir == 1:
                for row in range(t, b):
                    res.append(matrix[row][r - 1])
                    dir = 2
                r -= 1
            elif dir == 2:
                for col in range(r, l, -1):
                    res.append(matrix[b - 1][col - 1])
                    dir = 3
                b -= 1
            elif dir == 3:
                for row in range(b, t, -1):
                    res.append(matrix[row - 1][l])
                    dir = 0
                l += 1
        return res

    def test_1(self):
        self.assertEqual([1, 2, 3, 6, 9, 8, 7, 4, 5], self.spiralOrder([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]))
