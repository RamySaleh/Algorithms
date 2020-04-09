import heapq
from typing import List

from Helpers import helper as hlp
from Helpers import test_class
import re


class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def getKthSmallest(self, arr1, arr2, k) -> int:
        mergedArray = self.merge(arr1, arr2, k)
        return mergedArray[k - 1]

    def merge(self, arr1, arr2, k):
        res = []
        l = 0
        r = 0
        while l < len(arr1) and r < len(arr2):
            if arr1[l] <= arr2[r]:
                res.append(arr1[l])
                l += 1
            else:
                res.append(arr2[r])
                r += 1
            if len(res) == k:
                return res
        res += arr1[l:]
        res += arr2[r:]
        return res

    def test_1(self):
        self.assertEqual(4, self.getKthSmallest([1, 4, 6], [2, 3, 5], 4))

    def test_2(self):
        self.assertEqual(2, self.getKthSmallest([1, 4, 6, 8, 9, 12], [2, 3, 5, 7, 10, 11], 2))
