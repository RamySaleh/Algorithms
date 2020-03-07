# Min Adj Swaps to Make Palindrome
from typing import List

from Helpers import helper as hlp
from Helpers import test_class
import random
import collections


class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def getNoOfSwaps(self, s):
        swaps = 0
        if self.canBePalindrom(s):
            s = list(s)
            r = 0
            l = len(s) - 1
            while r < l:
                if s[r] != s[l]:  # need swapping
                    k = l
                    while s[r] != s[k]:
                        k -= 1
                    if k == r:  # no matching letter found
                        s[r], s[r + 1] = s[r + 1], s[r]
                        swaps += 1
                    else:   # matching letter found
                        while k < l:
                            s[k], s[k + 1] = s[k + 1], s[k]
                            k += 1
                            swaps += 1
                else:
                    r += 1
                    l -= 1
        else:
            return -1

        return swaps

    def canBePalindrom(self,s):
        dic = collections.Counter(s)
        odds = 0
        for val in dic.values():
            if val % 2 != 0:
                odds += 1
            if odds > 1:
                return False
        return True

    def test_1(self):
        self.assertEqual(3, self.getNoOfSwaps('mamad'))

    def test_2(self):
        self.assertEqual(-1, self.getNoOfSwaps('asflkj'))

    def test_3(self):
        self.assertEqual(2, self.getNoOfSwaps('aabb'))

    def test_4(self):
        self.assertEqual(1, self.getNoOfSwaps('ntiin'))
