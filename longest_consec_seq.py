# https://leetcode.com/problems/longest-consecutive-sequence/
from typing import List

from Helpers import helper as hlp
from Helpers import test_class


class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        res = 0
        for num in nums:
            if num - 1 not in num_set: # start of sequence
                newNum = num + 1
                counter = 1

                while newNum in num_set:
                    counter += 1
                    newNum += 1
                res = max(res, counter)

        return res

    def test_1(self):
        self.assertEqual(4, self.longestConsecutive([100, 4, 200, 1, 3, 2]))

    def test_2(self):
        self.assertEqual(4, self.longestConsecutive([5, 4, 3, 9, 8, 7, 10]))

    def test_3(self):
        self.assertEqual(2, self.longestConsecutive([4, 4]))

    def test_4(self):
        self.assertEqual(2, self.longestConsecutive([-8, -4, 9, 9, 4, 6, 1, -4, -1, 6, 8]))
