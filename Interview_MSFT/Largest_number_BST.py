#https://www.geeksforgeeks.org/largest-number-bst-less-equal-n/
from typing import List

from Helpers import helper as hlp
from Helpers import test_class
from Helpers import node as nd

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def largestNumber(self, root, N) -> List[List[int]]:
        res = float('-inf')
        while root:
            if N > root.val:
                res = max(res, root.val)
                root = root.right
            elif N < root.val:
                root = root.left
            else:
                return root.val
        return res


    def test_1(self):
        self.assertEqual(21, self.largestNumber(self.build_tree1(), 24))

    def test_2(self):
        self.assertEqual(3, self.largestNumber(self.build_tree1(), 4))

    def test_3(self):
        self.assertEqual(19, self.largestNumber(self.build_tree1(), 20))

    def test_4(self):
        self.assertEqual(5, self.largestNumber(self.build_tree1(), 6))

    def build_tree1(self):
        tree = nd.node(5)
        tree.left = nd.node(2)
        tree.right = nd.node(12)

        tree.left.left = nd.node(1)
        tree.left.right = nd.node(3)

        tree.right.left = nd.node(9)
        tree.right.right = nd.node(21)

        tree.right.right.left = nd.node(19)
        tree.right.right.right = nd.node(25)
        return tree