# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from Helpers import helper as hlp
from Helpers import test_class

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def searchRange(self, nums, target: int):
        l = 0
        r = len(nums) - 1
        res = []
        while l <= r:
            m = (r + l) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            if target == nums[m]:
                s = m
                e = m
                while e + 1 <= r and target == nums[e + 1]:
                    e += 1
                while s - 1 >= l and target == nums[s - 1]:
                    s -= 1
                res.append(s)
                res.append(e)
                break
        return res if res else [-1,-1]


    def test_1(self):
        self.assertEqual([3,4], self.searchRange([5,7,7,8,8,10], 8))

    def test_2(self):
        self.assertEqual([0,1], self.searchRange([2,2], 2))

    def test_3(self):
        self.assertEqual([0,2], self.searchRange([3,3,3], 3))