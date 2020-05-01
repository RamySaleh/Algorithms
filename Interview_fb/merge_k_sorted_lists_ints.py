# https://leetcode.com/problems/merge-k-sorted-lists/

from Helpers import profiler as prof
from Helpers import test_class
from typing import List
from Helpers import LList as ll

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def mergeKLists(self, lists):
        if not lists:
            return
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])
        return self.merge(l, r)

    def merge(self, l, r):
        out = []
        l_idx = 0
        r_idx = 0
        while l_idx < len(l) and r_idx < len(r):
            if l[l_idx] < r[r_idx]:
                out.append(l[l_idx])
                l_idx += 1
            else:
                out.append(r[r_idx])
                r_idx += 1
        out += l[l_idx:]
        out += r[r_idx:]
        return out

    def test_1(self):
        self.assertEqual([1,1,2,3,4,5], self.mergeKLists([[1,3,5], [1,2,4]]))

    def test_2(self):
        self.assertEqual([1,1,2,3,4,5,7,8,9], self.mergeKLists([[1,3,9], [1,2,7], [4,5,8]]))