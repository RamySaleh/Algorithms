import heapq
from typing import List

from Helpers import helper as hlp
from Helpers import test_class
import re


class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def print(self, n: int, res=[]) -> int:
        if n == 0:
            return res

        res.append(n)
        return self.print(n - 1, res)

    def print_r(self, n, res=[]) -> int:
        if n != 1:
            self.print_r(n - 1, res)
        res.append(n)
        return res

    def fac(self, n):
        if n == 1:
            return 1
        return n * self.fac(n-1)

    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)


    def test_1(self):
        self.assertEqual([3, 2, 1], self.print(3))

    def test_2(self):
        self.assertEqual([1, 2, 3], self.print_r(3))

    def test_fac_1(self):
        self.assertEqual(24, self.fac(4))

    def test_fib_1(self):
        self.assertEqual(3, self.fib(4))
