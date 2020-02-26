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
        self.nums = nums
        self.k = k

        #self.nums.sort(reverse=True)
        #self.heap = self.nums[:k]

        # Build a maxheap.
        n = len(self.nums)
        for i in range(n, -1, -1):
            self.heapify(self.nums, n, i)
        self.heap = self.nums[:k]

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:  # there is space
            self.heap.append(val)
        elif val > self.heap[-1]:  # no space, need to remove something
            self.heap.append(val)
            self.heapify(self.heap, len(self.heap), len(self.heap))
            self.heap.pop()
        return self.heap[-1]

    def add2(self, val: int) -> int:
        if len(self.heap) < self.k:  # there is space
            self._addToHeap(val)
        elif val > self.heap[-1]:  # no space, need to remove something
            self.heap.pop()
            self._addToHeap(val)
        return self.heap[-1]

    def _addToHeap(self, val):
        self.heap.append(val)
        idx = self._getIndex(val)
        self.heap[-1], self.heap[idx + 1] = self.heap[idx + 1], self.heap[-1]

    def heapify(self, arr, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2

        # See if left child of root exists and is
        # greater than root
        if l < n and arr[i] < arr[l]:
            largest = l

            # See if right child of root exists and is
        # greater than root
        if r < n and arr[largest] < arr[r]:
            largest = r

            # Change root, if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap

            # Heapify the root.
            self.heapify(arr, n, largest)

    def test_1(self):
        self.init(3, [4,5,8,2])
        self.assertEqual(4, self.add(6))
        self.assertEqual(4, self.add(3))
        self.assertEqual(5, self.add(5))
        self.assertEqual(5, self.add(10))
        self.assertEqual(8, self.add(9))
        self.assertEqual(8, self.add(4))