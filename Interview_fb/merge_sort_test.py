
from Helpers import profiler as prof
from Helpers import test_class
from typing import List
from Helpers import LList as ll

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def mergeSort(self, list):
        if len(list) <= 1:
            return list

        mid = len(list) // 2
        l = self.mergeSort(list[0:mid])
        r = self.mergeSort(list[mid:])
        return self.merge(l , r)

    def merge(self, l, r):
        out = []
        l_idx = 0
        r_idx = 0
        while l_idx < len(l) and r_idx < len(r):
            if l[l_idx] < r[r_idx]:
                out.append(l[l_idx])
                l_idx+=1
            else:
                out.append(r[r_idx])
                r_idx += 1
        out += l[l_idx:]
        out += r[r_idx:]
        return out

    def test_1(self):
        self.assertEqual([1,2,3,6,8], self.mergeSort([1,6,3,8,2]))