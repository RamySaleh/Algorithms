# https://leetcode.com/problems/valid-palindrome/
from typing import List

from Helpers import helper as hlp
from Helpers import test_class
import random


class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def isPalindrome(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            c1,c2 = s[l].lower(), s[r].lower()
            while not self.isValid(c1) and l < r:
                l += 1
                c1 = s[l].lower()
            while not self.isValid(c2) and l < r:
                r -= 1
                c2 = s[r].lower()
            if c1 != c2:
                return False
            l += 1
            r -= 1
        return True

    def isValid(self, c:str):
        if not c.isalnum():
            return False
        return True

    def test_1(self):
        self.assertEqual(True, self.isPalindrome('A man, a plan, a canal: Panama'))

    def test_2(self):
        self.assertEqual(True, self.isPalindrome('.,'))
