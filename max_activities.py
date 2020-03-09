import heapq
from typing import List

from Helpers import helper as hlp
from Helpers import test_class
import re


class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def maxActivities(self, arr) -> int:
        arr = sorted(arr, key=lambda x: x[2])
        last_act = arr[0]
        count = 1
        print(last_act)
        for i in range(1,len(arr)):
            if arr[i][1] >= last_act[2]:
                count += 1
                print(arr[i])
                last_act = arr[i]

        return count

    def test_1(self):
        self.assertEqual(4,
                         self.maxActivities([['A1',0,6],['A2',3,4],
                                             ['A3',1,2],['A4',5,8],
                                            ['A5',5,7],['A6',8,9]]))
