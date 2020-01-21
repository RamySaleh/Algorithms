#https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

from Helpers import helper as hlp
from Helpers import test_class

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def divisibleSumPairs(self, n, k, ar):
        mods = [0] * k
        for i in range(len(ar)):
            mods[ar[i] % k] += 1

        count = 0
        for i in range(int(k / 2) + 1):
            if i == 0:
                count += int(mods[i] * (mods[i] - 1) / 2) # for 0 the number of pairs : n * (n - 1) / 2
            elif float(i) == (k / 2):
                count += int(mods[int(i)] * (mods[int(i)] - 1) / 2) # if k is even then the item in the middle has no pairs with any other mods
            else:
                count += int(mods[i] * mods[k - i]) # for adj pairs : n * m

        return count

    def test_1(self):
        self.assertEqual(5, self.divisibleSumPairs(0,3,[1,3,2,6,1,2]))

    def test_2(self):
        self.assertEqual(15, self.divisibleSumPairs(0,3,[29,97,52,86,27,89,77,19,99,96]))

    def test_3(self):
        self.assertEqual(4, self.divisibleSumPairs(0,2,[5,9,10,7,4]))