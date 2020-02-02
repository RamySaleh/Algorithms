#https://leetcode.com/problems/move-zeroes/

from Helpers import helper as hlp
from Helpers import test_class
import re

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def moveZeroes(self, nums):
        zero = 0  # records the position of "0"
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

    def moveZeroes2(self, nums) -> None:
        stack = []
        for i in range(len(nums)):
            if nums[i] != 0:
                stack.append(nums[i])
                nums[i] = 0
        for i in range(len(stack)):
            nums[i] = stack[i]
        return nums

    def test_1(self):
        self.assertEqual([1,3,12,0,0], self.moveZeroes([0,1,0,3,12]))