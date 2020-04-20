# https://leetcode.com/problems/minimum-window-substring/

from Helpers import test_class
import collections
from typing import List


class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def minWindow(self, s, t) -> int:
        l=0
        res = ''
        dicT = collections.Counter(t)
        dicS = {}
        for r,c in enumerate(s):
            dicS[c] = dicS.get(c, 0) + 1
            while self.containsString(dicS, dicT):
                newStr = s[l:r + 1]
                if len(newStr) < len(res) or not res:
                    res = newStr
                dicS[s[l]] -= 1
                l += 1

        return res

    def containsString(self, dicS, dicT):
        for c,count in dicT.items():
            if c not in dicS or dicS[c] < count:
                return False
        return True

    def test_1(self):
        self.assertEqual('BANC', self.minWindow('ADOBECODEBANC', 'ABC'))
