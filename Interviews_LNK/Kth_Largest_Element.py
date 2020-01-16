#https://leetcode.com/explore/interview/card/linkedin/336/heap-queue-stack/2915/
import math
from typing import List

from Helpers import helper as hlp
from Helpers import test_class
import re

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = self.mergeSort(nums)
        return nums[k-1]

    def mergeSort(self, array):
        if len(array) <= 1:
            return array

        half = len(array) // 2
        left = self.mergeSort(array[:half])
        right = self.mergeSort(array[half:])

        return self.merge(left, right)

    def merge(self, left, right):
        left_index, right_index = 0, 0
        result = []
        while left_index < len(left) and right_index < len(right):
            if left[left_index] > right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

        result += left[left_index:]
        result += right[right_index:]
        return result

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        res = [-1] * k
        for n in nums:
            idx = -1
            for i in range(k):
                if n >= res[i]:
                    idx = i
                    break
            if idx > -1:
                res = res[:idx] + [n] + res[idx:-1]

        return res[k-1]

    def test_1(self):
        self.assertEqual(5, self.findKthLargest([3, 2, 1, 5, 6, 4, 5],2))

    def test_2(self):
        self.assertEqual(2, self.findKthLargest([4,2,1,3],3))

    def test_3(self):
        self.assertEqual(4, self.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))

    def test_4(self):
        self.assertEqual(4, self.findKthLargest(hlp.generate_array(1000,5000), 5000))
