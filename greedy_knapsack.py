import heapq
from typing import List

from Helpers import helper as hlp
from Helpers import test_class
import re


class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def knapsack(self, capacity,  arr) -> int:
        arr = sorted(arr, key=lambda x: x[1] // x[0],reverse=True)
        res = 0
        i = 0
        while capacity > 0 and i < len(arr):
            if arr[i][0] <= capacity:  # can carry all
                capacity -= arr[i][0]
                res += arr[i][1]
            else:  # need fraction
                fraction = (capacity / arr[i][0])
                res += fraction * arr[i][1]
                capacity = 0
            i += 1

        return res

    def test_1(self):
        self.assertEqual(240, self.knapsack(50, [[20, 100], [30, 120], [10, 60]]))

    def test_2(self):
        self.assertEqual(60, self.knapsack(10, [[20, 100], [30, 120], [10, 60]]))

    def test_3(self):
        self.assertEqual(280, self.knapsack(100, [[20, 100], [30, 120], [10, 60]]))

    def test_4(self):
        self.assertEqual(30, self.knapsack(5, [[20, 100], [30, 120], [10, 60]]))
