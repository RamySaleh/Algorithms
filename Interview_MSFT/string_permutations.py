from typing import List

from Helpers import helper as hlp
from Helpers import test_class
import random


class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def getPermutations(self, s):
        res = []
        self.permute('', s, res)
        return res

    def permute(self, prefix, suffix, res):
        if not suffix:
            res.append(prefix)
        for i, c in enumerate(suffix):
            self.permute(prefix + c, suffix[:i] + suffix[i + 1:], res)

    def test_1(self):
        self.assertEqual(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'], self.getPermutations('abc'))
