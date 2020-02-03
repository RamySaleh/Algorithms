#https://leetcode.com/problems/find-bottom-left-tree-value/
from typing import List

from Helpers import helper as hlp
from Helpers import test_class
from Helpers import node as nd

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def findBottomLeftValue(self, root) -> int:
        stack = [[root]]
        nodes = []
        while stack:
            children = []
            nodes = stack.pop()
            for node in nodes:
                if node:
                    if node.left:
                        children.append((node.left))
                    if node.right:
                        children.append((node.right))
            if children:
                stack.append(children)

        return nodes[0].val

    def test_1(self):
        self.assertEqual(4, self.findBottomLeftValue(self.build_tree1()))


    def build_tree1(self):
        tree = nd.node(1)
        tree.left = nd.node(2)
        tree.right = nd.node(3)

        tree.left.left = nd.node(4)
        tree.left.right = nd.node(5)
        return tree