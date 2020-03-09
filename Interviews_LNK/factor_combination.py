# https://leetcode.com/problems/factor-combinations/
from typing import List

from Helpers import helper as hlp
from Helpers import test_class
import re

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def getFactors(self, n: int) -> List[List[int]]:
        return self.rec(n, 2, [], [])

    def rec(self, n, i, factors, res):
        while i*i <= n:
            if n % i == 0:
                res.append(factors + [i, n//i])
                self.rec(n // i, i, factors + [i], res)
            i += 1
        return res

    def getFactors2(self,  n: int) -> List[List[int]]:
        res = []
        i = 2
        while i*i <= n:
            arr = []
            stack = [n]
            while stack:
                n = stack.pop()
                if n % i == 0:
                    arr += [i]
                    stack.append(n//i)
            i += 1
            res.append(arr)
        return res

    def test_1(self):
        self.assertEqual([[2,6],[2,2,3],[3,4]], self.getFactors(12))
