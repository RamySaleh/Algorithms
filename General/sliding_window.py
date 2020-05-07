# https://leetcode.com/problems/continuous-subarray-sum/submissions/

from Helpers import helper as hlp
from Helpers import test_class
import re


class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def arraySum_fixedWindow(self, nums, k, w):
        cur_sum = 0
        for i,n in enumerate(nums):
            cur_sum += n
            if i >= w - 1:  # reached window size
                if cur_sum == k:
                    return True
                cur_sum -= nums[i + 1 - w]
        return False

    def arraySum_dynamicWindow(self, nums, k):
        l = 0
        cur_sum = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            while cur_sum > k:
                cur_sum -= nums[l]
                l += 1
            if cur_sum == k:
                return True
        return False

    def arrayMaxSum(self, nums):
        l = 0
        cur_sum = 0
        max_sum = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            while cur_sum < 0 and l < r:
                cur_sum = 0
                l += 1
            max_sum = max(max_sum, cur_sum)
        return max_sum

    def test_fw_1(self):
        self.assertEqual(True, self.arraySum_fixedWindow([23, 2, 4, 6, 7], 6, 2))

    def test_fw_2(self):
        self.assertEqual(True, self.arraySum_fixedWindow([23, 2, 4, 6, 7], 12, 3))

    def test_dw_1(self):
        self.assertEqual(True, self.arraySum_dynamicWindow([23, 2, 4, 6, 7], 6))

    def test_dw_2(self):
        self.assertEqual(True, self.arraySum_dynamicWindow([23, 2, 4, 6, 7], 17))

    def test_max_sum_1(self):
        self.assertEqual(10, self.arrayMaxSum([1, 2, -10 , 3, 7]))

    def test_max_sum_2(self):
        self.assertEqual(9, self.arrayMaxSum([1, 2, -10, -1 , 3, -1, 7]))
