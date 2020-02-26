# https://leetcode.com/problems/continuous-subarray-sum/submissions/

from Helpers import helper as hlp
from Helpers import test_class
import re


class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def checkSubarraySum(self, nums, k):
        # (sum1 - sum2) % k = 0 , sum1 = sum(0 to 5), sum2 = sum(0 to 3) -> sum(4 to 5)
        # sum1 % k - sum2 % k = 0
        # sum1 % k = sum2 % k
        dic = {0: -1}  # to get the length of the whole array we subtract the index i - 1
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if k != 0:
                mod = sum % k
            else:
                mod = sum

            if mod in dic:  # we have seen this mod before
                if i - dic[mod] > 1:  # the length of the sub array >= 2 items
                    return True
            else:
                dic[mod] = i
        return False

    def test_1(self):
        self.assertEqual(True, self.checkSubarraySum([23, 2, 4, 6, 7], 6))

    def test_2(self):
        self.assertEqual(False, self.checkSubarraySum([0, 1, 0], 0))

    def test_3(self):
        self.assertEqual(True, self.checkSubarraySum([0, 0], 0))

    def test_4(self):
        self.assertEqual(False, self.checkSubarraySum([23,2,6,4,7], 0))
