# https://leetcode.com/problems/powx-n/

from Helpers import helper as hlp
from Helpers import test_class

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def myPow(self, x: float, n: int):
        ans = 0
        return ans


    def test_1(self):
        self.assertEqual(1024.0000, self.myPow(2.0000, 10))