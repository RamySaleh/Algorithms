# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

from Helpers import helper as hlp
from Helpers import test_class
from typing import List
import collections


class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def areTheyEqual(self, a: List[str], b: List[str] ) -> int:
        res = False
        res = collections.Counter(a) == collections.Counter(b)
        return res


    def test_1(self):
        self.assertEqual(True ,self.areTheyEqual([1,2,3,4], [1,4,3,2]))

    def test_2(self):
        self.assertEqual(True ,self.areTheyEqual([1,2,3,4], [4,2,3,1]))