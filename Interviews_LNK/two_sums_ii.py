from Helpers import helper as hlp
from Helpers import test_class
import functools


class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def twoSum(self, nums, target: int):
        lookup = {num:i for i,num in enumerate(nums)}
        count = functools.reduce(lambda cnt, num: cnt + 1 if target - num in lookup else cnt, nums)
        return count // 2

    def test_1(self):
        self.assertEqual(1, self.twoSum([2, 7, 11, 15], 9))

    def test_2(self):
        self.assertEqual(4, self.twoSum([1, 5, 3, 3, 3], 6))
