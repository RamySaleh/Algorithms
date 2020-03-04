# https://leetcode.com/problems/closest-binary-search-tree-value-ii/
import math

from Helpers import helper as hlp
from Helpers import test_class
from Helpers import node as nd

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def closestKValues(self, root, target: float, k: int):
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        # get smallest k nodes based on the difference between node.val and target using heapq
        # res = [node for node in heapq.nsmallest(k, res, key=lambda x: abs(x - target))]
        # return res
        res = sorted(res, key=lambda x: abs(x - target))
        return res[:k]

    def test_1(self):
        self.assertEqual([4,3], self.closestKValues(self.build_tree1(), 3.5, 2))

    def test_2(self):
        self.assertEqual([1], self.closestKValues(self.build_tree2(), 3, 1))

    def build_tree1(self):
        tree = nd.node(4)
        tree.left = nd.node(2)
        tree.right = nd.node(5)

        tree.left.left = nd.node(1)
        tree.left.right = nd.node(3)
        return tree

    def build_tree2(self):
        tree = nd.node(1)
        tree.right = nd.node(8)
        return tree