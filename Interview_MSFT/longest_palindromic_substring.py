from typing import List

from Helpers import helper as hlp
from Helpers import test_class
import random

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0

        for i in range(len(s)):
            len1 = self.expandFromMiddle(s, i, i)
            len2 = self.expandFromMiddle(s, i, i + 1)
            ln = max(len1,len2)
            if ln > end - start:
                start = i - (ln - 1) // 2
                end = i + (ln // 2)
        return s[start : end + 1]

    def expandFromMiddle(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1

    def test_1(self):
        self.assertEqual('bab',self.longestPalindrome('babad'))

    def test_2(self):
        self.assertEqual('bab',self.longestPalindrome('cbabd'))

    def test_3(self):
        self.assertEqual('a',self.longestPalindrome('a'))

    def test_4(self):
        self.assertEqual('bb',self.longestPalindrome('cbbd'))

    def test_5(self):
        self.assertEqual('ccc',self.longestPalindrome('ccc'))

