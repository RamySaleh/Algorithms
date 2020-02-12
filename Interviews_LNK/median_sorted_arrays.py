#https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import List

from Helpers import helper as hlp
from Helpers import test_class

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = r = m = 0
        res = []
        while l < len(nums1) and r < len(nums2):
            if nums1[l] > nums2[r]:
                res.append(nums2[r])
                r += 1
            else:
                res.append((nums1[l]))
                l += 1

        res += nums1[l:] + nums2[r:]
        middle = len(res) // 2

        if len(res) % 2 != 0:  # odd
            m = res[middle]
        else:  # even
            m = (res[middle] + res[middle - 1]) / 2
        return m

    def test_1(self):
        self.assertEqual(2.5, self.findMedianSortedArrays([1,3],[2,4]))