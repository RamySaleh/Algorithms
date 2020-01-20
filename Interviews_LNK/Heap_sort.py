from Helpers import helper as hlp
from Helpers import test_class
import re

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def heapSort(self, arr):
        n = len(arr)

        # Build a maxheap.
        for i in range(n, -1, -1):
            self.heapify(arr, n, i)

        # One by one extract elements
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # swap
            self.heapify(arr, i, 0)

        return arr


    # To heapify subtree rooted at index i.
    # n is size of heap
    def heapify(self, arr, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2

        # See if left child of root exists and is
        # greater than root
        if l < n and arr[i] < arr[l]:
            largest = l

        # See if right child of root exists and is
        # greater than root
        if r < n and arr[largest] < arr[r]:
            largest = r

        # Change root, if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        self.heapify(arr, n, largest)

    def test_1(self):
        self.assertEqual([1,2,3,4,7,9], self.heapSort([7,3,9,1,2,4]))

    def test_2(self):
        self.assertEqual([4], self.heapSort(hlp.generate_array(1000,5000)))