# https://leetcode.com/problems/max-points-on-a-line/
import heapq
from typing import List

from Helpers import helper as hlp
from Helpers import test_class
import re

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        dic = {}
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                key = ''
                if points[j][0] == points[i][0]:
                    #m = -10 * points[j][0]
                    m = 'v'
                    c = points[j][0]
                elif points[j][1] == points[i][1]:
                    #m = 10 * points[j][1]
                    m = 'h'
                    c = points[j][1]
                else:
                    # m = y2 - y1 / x2 - x1        y = mx + c
                    m = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
                    c = points[j][1]
                if m == 5:
                    print(points[i])
                    print(points[j])
                    print(str(c) + '----')
                key = f'{m},{c}'
                dic.setdefault(key, set()).update([i, j])
                res = max(res, len(dic[key]))
        return res

    def test_1(self):
        self.assertEqual(3, self.maxPoints([[1,1],[2,2],[3,3]]))

    def test_2(self):
        self.assertEqual(4, self.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))

    def test_3(self):
        self.assertEqual(3, self.maxPoints([[1,1],[2,1],[2,2],[1,4],[3,3]]))

    def test_4(self):
        self.assertEqual(6, self.maxPoints([[0,-12],[5,2],[2,5],[0,-5],[1,5],[2,-2],[5,-4],[3,4],[-2,4],[-1,4],[0,-5],[0,-8],[-2,-1],[0,-11],[0,-9]]))