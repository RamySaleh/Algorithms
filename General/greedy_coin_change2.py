import heapq
from typing import List

from Helpers import helper as hlp
from Helpers import test_class
import re


class Wallet(test_class.test_class):

    def setUp(self):
        super().setUp()
        self.wallet = []

    def loadWalletFromFile(self):
        f = open('../resources/Wallet.txt', 'r')
        x = f.readline()
        self.wallet = eval(x)
        f.close()

    def getBalance(self):
        return self.wallet, sum(self.wallet)

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


    def test_loadWalletFromFile(self):
        self.loadWalletFromFile()
        self.assertEqual([1,10,50,100,200,200,1000], self.wallet)

    def test_getBalance(self):
        self.loadWalletFromFile()
        self.assertEqual(([1,10,50,100,200,200,1000],1561), self.getBalance())

    def test_cc1(self):
        self.assertEqual(0, self.coinChange(6, [1,10,50,100,200,200,1000]))
