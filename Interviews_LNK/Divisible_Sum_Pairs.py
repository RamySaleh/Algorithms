#https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

from Helpers import helper as hlp
from Helpers import test_class

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def divisibleSumPairs(self, n, k, ar):
        lookup = {}
        mod_arr = []
        i = 0
        for num in ar:
            if num not in lookup:
                lookup[num] = [i]
            else:
                lookup[num].append(i)
            i += 1
            mod_arr.append(num % k)

        counter = 0
        res = {}
        for num in mod_arr:
            adj = k - num
            if adj in lookup:
                counter += len(lookup[adj])

        return counter



    def test_1(self):
        self.assertEqual(5, self.divisibleSumPairs(0,3,[1,3,2,6,1,2]))