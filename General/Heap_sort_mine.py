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

    def sort_heap2(self, arr, k = -1):
        n = len(arr)
        if k == -1:
            k = n

        while k > 0:
            # swap first with last
            arr[0], arr[n-1] = arr[n-1], arr[0]
            # array is smaller by 1 (last item is deleted)
            n -= 1
            i = 0

            while i * 2 + 1 < n:
                l = i * 2 + 1 # left child
                r = i * 2 + 2 # right child
                c = l if (arr[l] > arr[r]) or (r > n-1) else r

                if arr[c] >= arr[i]:
                    arr[i], arr[c] = arr[c], arr[i]
                    i += c
                else:
                    break
            k -= 1

    def heapSort(self, arr, n = -1):
        n = len(arr)

        for i in range(n - 1, 0, -1):

            # swap value of first indexed
            # with last indexed
            arr[0], arr[i] = arr[i], arr[0]

            # maintaining heap property
            # after each swapping
            j, index = 0, 0

            while True:
                index = 2 * j + 1

                # if left child is smaller than
                # right child point index variable
                # to right child
                if (index < (i - 1) and
                        arr[index] < arr[index + 1]):
                    index += 1

                # if parent is smaller than child
                # then swapping parent with child
                # having higher value
                if index < i and arr[j] < arr[index]:
                    arr[j], arr[index] = arr[index], arr[j]

                j = index
                if index >= i:
                    break

        return arr


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

    def test_4(self):
        self.assertEqual([5], self.heapSort([3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]))

    def test_5(self):
        self.assertEqual([1,1,1,1,2,2,2,3,3,3,4,5,7], self.heapSort([3,2,3,1,2,4,5,7,2,3,1,1,1]))