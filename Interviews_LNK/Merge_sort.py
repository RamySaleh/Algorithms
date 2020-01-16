from Helpers import helper as hlp
from Helpers import test_class
import re

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def mergeSort(self, nums, asc = True):

        if len(nums) <= 1:
            return nums

        s = 0
        e = len(nums)
        m = (s + e) // 2

        l = self.mergeSort(nums[:m], asc)
        r = self.mergeSort(nums[m:], asc)

        return self.merge(l,r, asc)

    def merge(self, l, r, asc):
        l_index = r_index = 0
        res = []

        while l_index < len(l) and r_index < len(r):
            if (asc and l[l_index] < r[r_index]) or (not asc and l[l_index] > r[r_index]):
                res.append(l[l_index])
                l_index+=1
            else:
                res.append(r[r_index])
                r_index += 1

        res += l[l_index:]
        res += r[r_index:]

        return res


    def test_1(self):
        self.assertEqual([1,2,3,4,7,9], self.mergeSort([7,3,9,1,2,4], True))

    def test_2(self):
        self.assertEqual([9,7,4,3,2,1], self.mergeSort([7,3,9,1,2,4], False))

    def test_3(self):
        self.assertEqual([4], self.mergeSort(hlp.generate_array(1000,5000)))