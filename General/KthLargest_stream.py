# https://leetcode.com/problems/kth-largest-element-in-a-stream/submissions/
import heapq
from typing import List

from Helpers import helper as hlp
from Helpers import test_class
import re

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def init(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]

    def test_1(self):
        self.init(3, [4,5,8,2])
        self.assertEqual(4, self.add(3))
        self.assertEqual(5, self.add(5))
        self.assertEqual(5, self.add(10))
        self.assertEqual(8, self.add(9))
        self.assertEqual(8, self.add(4))