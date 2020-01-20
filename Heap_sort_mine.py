from Helpers import helper as hlp
from Helpers import test_class
import re

class Solution(test_class.test_class):

    # left = i * 2
    # right = i * 2 + 1
    # parent = i // 2
    def setUp(self):
        super().setUp()

    def heapSort(self, arr):
        self.build_heap(arr)
        self.sort_heap(arr)
        return arr

    def build_heap(self, arr):
        for i in range(len(arr)):
            while i > 0:
                p = i // 2  # parent
                if arr[i] >= arr[p]:
                    arr[i], arr[p] = arr[p], arr[i]
                i = p
        return arr

    def sort_heap(self, arr, n = 0):
        n = len(arr)
        i = 0
        while n > 0:
            # swap first with last
            arr[0], arr[n-1] = arr[n-1], arr[0]
            n -= 1
            while i * 2 + 1 < n:
                c1 = i * 2 + 1 # child 1
                c2 = i * 2 + 2 # child 2
                c = c1 if (arr[c1] > arr[c2]) or (c2 > n-1) else c2

                if arr[c] >= arr[i]:
                    arr[i], arr[c] = arr[c], arr[i]
                    i += c
                else:
                    break
            i = 0


    def get_kth(self, arr, k):
        self.build_heap(arr)
        self.sort_heap(arr, k)
        return arr[len(arr) - k]

    def test_1(self):
        self.assertEqual([40,30,20,15,10], self.build_heap([10,20,15,30,40]))

    def test_2(self):
        self.assertEqual([6,5,4,2,1,3], self.build_heap([3,2,1,5,6,4]))

    def test_3(self):
        self.assertEqual([6,5,4,1,2,3,0], self.build_heap([5,2,4,1,3,6,0]))

    def test_1_1(self):
        self.assertEqual([10,15,20,30,40], self.heapSort([10,20,15,30,40]))

    def test_3_1(self):
        self.assertEqual([0,1,2,3,4,5,6], self.heapSort([5,2,4,1,3,6,0]))

    def test_3_2(self):
        self.assertEqual(3, self.get_kth([5,2,4,1,3,6,0], 4))