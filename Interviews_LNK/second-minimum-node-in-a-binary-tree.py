#https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
from typing import List

from Helpers import helper as hlp
from Helpers import test_class
from Helpers import node as nd

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def findSecondMinimumValue(self, root) -> int:
        uniques = set()
        self.dfs(root, uniques)

        min1, ans = root.val, float('inf')
        for v in uniques:
            if min1 < v < ans:
                ans = v

        return ans if ans < float('inf') else -1

    def dfs(self, node, uniques):
        if node:
            uniques.add(node.val)
            self.dfs(node.left, uniques)
            self.dfs(node.right, uniques)

    def test_1(self):
        self.assertEqual(5, self.findSecondMinimumValue(self.build_tree1()))


    def build_tree1(self):
        tree = nd.node(2)
        tree.left = nd.node(2)
        tree.right = nd.node(5)

        tree.right.left = nd.node(5)
        tree.right.right = nd.node(7)
        return tree