# https://leetcode.com/problems/search-a-2d-matrix-ii/
from typing import List

from Helpers import helper as hlp
from Helpers import test_class
import random
import collections


class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def searchMatrix2(self, matrix, target):
        if not matrix:
            return False

        l = 0
        r = len(matrix[0]) - 1
        t = 0
        b = len(matrix) - 1
        while l <= r:
            m_r = (t + b) // 2
            m_c = (l + r) // 2
            if target == matrix[m_r][m_c]:
                return True
            elif target < matrix[m_r][m_c]:
                b = m_r - 1
                r = m_c - 1
            elif target > matrix[m_r][m_c]:
                t = m_r + 1
                l = m_c + 1
        return False

    def searchMatrix(self, matrix, target):
        if not matrix:
            return False

        h = len(matrix)
        w = len(matrix[0])
        i = h - 1
        j = 0
        while 0 <= i < h and 0 <= j < w:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        return False

    def test_1(self):
        self.assertEqual(True, self.searchMatrix([
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ], 5))

    def test_1a(self):
        self.assertEqual(True, self.searchMatrix([
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ], 3))

    def test_2(self):
        self.assertEqual(True, self.searchMatrix([[5], [6]], 6))

    def test_3(self):
        self.assertEqual(True, self.searchMatrix([[-5]], 2))
