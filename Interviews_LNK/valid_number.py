#https://leetcode.com/explore/interview/card/linkedin/339/array-and-strings/1968/

from Helpers import helper as hlp
from Helpers import test_class
import re

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def isNumber(self, s: str) -> bool:
        s = s.strip()
        p = r'^[+-]?(\d+(\.\d*)?|\.\d+)(e[+-]?\d+)?$'
        matchObj = re.match(p, s, re.M|re.I)
        if matchObj:
            return True

    def test_1(self):
        self.assertEqual(True, self.isNumber('+55.55e33'))

    def test_2(self):
        self.assertEqual(True, self.isNumber(".7e-33"))