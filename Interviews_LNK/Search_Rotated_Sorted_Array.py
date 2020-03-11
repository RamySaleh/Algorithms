# https://leetcode.com/problems/search-in-rotated-sorted-array/

from Helpers import helper as hlp
from Helpers import test_class

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def search(self, nums, target: int):
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (r + l) // 2
            if target == nums[m]:
                return m
            elif nums[m] >= nums[l]:  # not pivot
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1


    def test_1(self):
        self.assertEqual(4, self.search([4,5,6,7,0,1,2], 0))

    def test_2(self):
        self.assertEqual(-1, self.search([1,3], 0))

    def test_3(self):
        self.assertEqual(0, self.search([5,1,3], 5))