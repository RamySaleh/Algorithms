from typing import List

from Helpers import helper as hlp
from Helpers import test_class
import random

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def longestPalindrome(self, s: str) -> str:
        dic, res = {}, ''
        if s:
            res = s[0]
        for i,c in enumerate(s):
            dic.setdefault(c, []).append(i)

        for c,indx in dic.items():
            if(len(indx)) >= 2:
                for i in range(len(indx)):
                    for j in range(len(indx) - 1, i, -1):
                        if indx[j] - indx[i] + 1 > len(res):
                            if self.isPalindrom(s, indx[i], indx[j]):
                                res = s[indx[i] : indx[j] + 1]
                        else:
                            break
        return res

    def isPalindrom(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

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

