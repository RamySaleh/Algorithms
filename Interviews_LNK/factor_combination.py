# https://leetcode.com/problems/factor-combinations/
from typing import List

from Helpers import helper as hlp
from Helpers import test_class
import re

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        self.rec(n, [], res)
        return res

    def rec(self, n, factors, res):
        if n == 1:
            res.append(factors)
            return

        for i in range(2, n + 1):
            if n % i == 0:
                res += factors + [i, n/i]
                self.rec(n // i, factors + [i], res)

    def test_1(self):
        self.assertEqual([[2,6],[2,2,3],[3,4]], self.getFactors(12))
