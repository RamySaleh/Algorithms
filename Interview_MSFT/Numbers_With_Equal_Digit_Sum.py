#https://leetcode.com/discuss/interview-question/365872/
from typing import List

from Helpers import helper as hlp
from Helpers import test_class
from Helpers import profiler as prof
import collections

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()
        self.test_array = hlp.generate_array(1000000000,200000)

    def getMaxSum2(self, arr):  # N x A
        dic = {}
        max_sum = -1
        for n in arr:  # N
            s = self.getDigitsSum2(n)  # A
            if s not in dic:
                dic[s] = n
            else:
                max_sum = max(max_sum, dic[s] + n)
                dic[s] = max(dic[s], n)  # dic[s] always has the maximum number
        return max_sum

    def getDigitsSum2(self, a):
        a = abs(a)
        res = 0
        while a > 0:
            res += a % 10
            a = a // 10
        return res

    def getMaxSum(self, arr):  # N x A
        dic = {}
        for n in arr:  # N
            s = self.getDigitsSum(n)  # A
            dic[s] = dic.get(s, [float('-inf'), float('-inf')])
            if n > dic[s][0]:
                dic[s][1] = dic[s][0]
                dic[s][0] = n
            elif dic[s][1] < n < dic[s][0]:
                dic[s][1] = n

        max_sum = -1
        for nums in dic.values():
            if len(nums) < 2:
                continue
            max_sum = max(max_sum, sum(nums))

        return max_sum

    def getDigitsSum(self, num):
        s = 0
        num = str(num)
        for c in num:
            s += int(c)
        return s

    def test_1(self):
        self.assertEqual(93, self.getMaxSum([51,71,17,42]))

    def test_1_1(self):
        self.assertEqual(151, self.getMaxSum([51,71,17,42,80]))

    def test_2(self):
        self.assertEqual(102, self.getMaxSum([42,33,60]))

    def test_3(self):
        self.assertEqual(-1, self.getMaxSum([51,32,43]))

    def test_z(self):
        self.assertEqual(10, self.getMaxSum(self.test_array))

    def test_z2(self):
        self.assertEqual(10, self.getMaxSum2(self.test_array))
