#https://leetcode.com/explore/interview/card/linkedin/339/array-and-strings/2907/

from Helpers import helper as hlp
from Helpers import test_class

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def twoSum(self, nums, target: int):
        lookup = {}
        idx = 0
        for num in nums:
            lookup[num] = idx
            idx += 1

        idx = 0
        for num in nums:
            adj = target - num
            if adj in lookup and idx != lookup[adj]:
                return [idx, lookup[adj]]
            idx += 1

    def test_1(self):
        self.assertEqual([0,1], self.twoSum([2, 7, 11, 15],9))

    def test_2(self):
        self.assertEqual([0,1], self.twoSum([3,3],6))