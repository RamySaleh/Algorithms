# https://leetcode.com/problems/merge-intervals/


from Helpers import helper as hlp
from Helpers import test_class
from typing import List


class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def merge(self, intervals) -> List[List[int]]:
        if not intervals:
            return []

        intervals = sorted(intervals, key=lambda x:x[0])
        res = []
        min_s = intervals[0][0]
        max_e = intervals[0][1]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if cur[0] <= max_e and cur[1] >= min_s:  # overlapping
                min_s = min(min_s, cur[0])
                max_e = max(max_e, cur[1])
            else:
                res.append([min_s, max_e])
                min_s = cur[0]
                max_e = cur[1]
        res.append([min_s, max_e])
        return res

    def test_1(self):
        self.assertEqual([[1, 6], [8, 10], [15, 18]], self.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))

    def test_2(self):
        self.assertEqual([[1, 5]], self.merge([[1, 4], [4, 5]]))

    def test_3(self):
        self.assertEqual([[0, 4]], self.merge([[1, 4], [0, 4]]))

    def test_4(self):
        self.assertEqual([[0, 0], [1, 4]], self.merge([[1, 4], [0, 0]]))

    def test_5(self):
        self.assertEqual([[0,4]], self.merge([[1,4],[0,1]]))

    def test_6(self):
        self.assertEqual([[1,10]], self.merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
