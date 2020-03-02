
from typing import List

from Helpers import helper as hlp
from Helpers import test_class
from Helpers import profiler as prof
import collections

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def getMaxPaths(self, arr):
        dic, res = {}, None
        for c in arr:
            c1, c2 = c[0], c[1]
            dic.setdefault(c1, set()).add(c2)
            dic.setdefault(c2, set()).add(c1)

        max_sum = 0
        for c in arr:
            c1_links, c2_links = len(dic[c[0]]), len(dic[c[1]])
            pair_sum = c1_links + c2_links
            if pair_sum > max_sum:
                max_sum = max(max_sum, pair_sum)
                res = c
        return res


    def test_1(self):
        self.assertEqual([3,5], self.getMaxPaths([[1,2],[3,4],[3,5],[5,6],[5,7],[2,3]]))