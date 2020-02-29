#https://leetcode.com/problems/find-the-celebrity/
from typing import List

from Helpers import helper as hlp
from Helpers import test_class
import collections

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def isIsomorphic(self, s, t):
        # location of each char in string 1 == location of each char in string 2
        # means string 1 chars can be replaced to reach string 2
        s_map = [s.find(i) for i in s]
        t_map = [t.find(i) for i in t]
        return s_map == t_map


    def test_1(self):
        self.assertEqual(1, self.isIsomorphic("egg","add"))