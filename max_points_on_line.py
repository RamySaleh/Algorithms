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
        if not points:
            return 0
        if len(points) == 1:
            return 1
        if len(points) == 2:
            return 2
        dic = {}
        res = 0
        h = len(points)
        for i in range(h):
            for j in range(i + 1, h):
                if points[j][0] == points[i][0]:
                    m = -10 * points[j][0]
                elif points[j][1] == points[i][1]:
                    m = 10 * points[j][1]
                else:
                    m = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
                dic[m] = dic.get(m, set())
                dic[m].add(i)
                dic[m].add(j)
                res = max(res, len(dic[m]))
        return res

    def test_1(self):
        self.assertEqual(3, self.maxPoints([[1,1],[2,2],[3,3]]))

    def test_2(self):
        self.assertEqual(4, self.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))

    def test_3(self):
        self.assertEqual(3, self.maxPoints([[1,1],[2,1],[2,2],[1,4],[3,3]]))

    def test_4(self):
        self.assertEqual(6, self.maxPoints([[0,-12],[5,2],[2,5],[0,-5],[1,5],[2,-2],[5,-4],[3,4],[-2,4],[-1,4],[0,-5],[0,-8],[-2,-1],[0,-11],[0,-9]]))