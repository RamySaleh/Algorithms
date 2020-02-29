#https://leetcode.com/problems/find-the-celebrity/
from typing import List

from Helpers import helper as hlp
from Helpers import test_class

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def findCelebrity(self, n: int) -> int:
        for a in range(n):  # for each person
            knowsNoOne = True
            for b in range(n):
                # person a knows someone else
                # or someone does not know him
                if (knows(a, b) and a != b) or not knows(b, a):
                    knowsNoOne = False
                    break

            if knowsNoOne:
                return a
        return -1

    def test_1(self):
        self.assertEqual(1, self.findCelebrity([[1,1,0],[0,1,0],[1,1,1]]))