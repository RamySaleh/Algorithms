from typing import List

from Helpers import helper as hlp
from Helpers import test_class
import random


class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def getMoves(self, str):
        a = b = moves = 0
        for c in str:
            if c == 'a':
                a += 1
                b = 0
            else:
                b += 1
                a = 0
            if a == 3 or b == 3:
                moves += 1
                a = b = 0
        return moves

    def test_1(self):
        self.assertEqual(1, self.getMoves('baaaaa'))

    def test_2(self):
        self.assertEqual(2, self.getMoves('baaabbaabbba'))

    def test_3(self):
        self.assertEqual(0, self.getMoves('baabbaa'))
