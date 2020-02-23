
from Helpers import helper as hlp
from Helpers import test_class
import re

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def combinationSum(self, arr):
        res = sum = 0
        for i in range(len(arr)):
            if sum < 0:
                sum = 0
            sum += arr[i]
            res = max(res, sum)
        return res

    def combinationSum2(self, arr):
        max_sum = 0

        for i in range(len(arr)):
            cur_sum = arr[i]
            for j in range(i+1, len(arr), 1):
                cur_sum += arr[j]
                max_sum = max(cur_sum,max_sum)

        return max_sum

    def test_1(self):
        self.assertEqual(10, self.combinationSum([1, 2, -10 , 3, 7]))

    def test_2(self):
        self.assertEqual(10, self.combinationSum([3, 7, -10 , 1, 2]))

    def test_3(self):
        self.assertEqual(7, self.combinationSum([-2, -3, 4 , -1, -2, 1, 5, -3]))

    def test_4(self):
        self.assertEqual(10, self.combinationSum([3, 7, -9 , 1, 2]))

    def test_5(self):
        self.assertEqual(10, self.combinationSum([4, 1, -4 , 4, 5]))