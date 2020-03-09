import heapq
from typing import List

from Helpers import helper as hlp
from Helpers import test_class
import re

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def coinChange(self, target, coins) -> int:
        coins.sort()
        sum = 0
        change = 0
        for i in range(len(coins)):
            sum += coins[i]
            coins[i] = 0
            if sum >= target:
                change = sum - target
                coins[i] = change
                break
        print(coins)
        return change

    def test_1(self):
        self.assertEqual(0, self.coinChange(6, [1,10,5,100]))

    def test_2(self):
        self.assertEqual(9, self.coinChange(7, [1,10,5,100]))

    def test_3(self):
        self.assertEqual(80, self.coinChange(36, [1,10,5,100]))
