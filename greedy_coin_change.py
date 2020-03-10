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
        return change

    def minCoins2(self, target, coins) -> int:
        coins.sort(reverse=True)
        ans = []
        count = 0
        larger_coin = None
        for i in range(len(coins)):
            if target >= coins[i]:
                target -= coins[i]
                ans.append(coins[i])
                coins[i] = 0
                count += 1
            elif target == 0:
                break
            else:
                larger_coin = i
        if target > 0 and larger_coin is not None:
            count += 1
            coins[larger_coin] -= target

        print(coins)
        print(ans)
        return count

    def minCoins(self, target, coins) -> int:
        coins.sort(reverse=True)
        ans = []
        i = 0
        while target > 0:
            if target >= coins[i]:
                target -= coins[i]
                ans.append(coins[i])
            else:
                i += 1
        print(ans)
        return len(ans)

    def test_cc1(self):
        self.assertEqual(0, self.coinChange(6, [1, 10, 5, 100]))

    def test_cc2(self):
        self.assertEqual(9, self.coinChange(7, [1, 10, 5, 100]))

    def test_cc3(self):
        self.assertEqual(80, self.coinChange(36, [1, 10, 5, 100]))

    def test_mc1(self):
        self.assertEqual(2, self.minCoins(6, [1, 10, 5, 100]))

    def test_mc2(self):
        self.assertEqual(3, self.minCoins(16, [1, 10, 5, 100]))

    def test_mc3(self):
        self.assertEqual(2, self.minCoins(20, [1, 10, 5, 100]))

    def test_mc4(self):
        self.assertEqual(3, self.minCoins(121, [1, 10, 5, 2, 60, 20, 100, 500, 1000]))

    def test_mc5(self):
        self.assertEqual(5, self.minCoins(2045, [1, 10, 5, 2, 60, 20, 100, 500, 1000]))
