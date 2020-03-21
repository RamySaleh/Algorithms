# https://leetcode.com/discuss/interview-question/algorithms/125110/tournament-tree-problem?fbclid=IwAR3oPVpCjaZeFPzWYDh4xs-n1HIZVZ8pf8Ii52hMehEGdfQAmx7p-WUbyo4
from typing import List

from Helpers import helper as hlp
from Helpers import test_class
from Helpers import node as nd

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def secondMin(self, root) -> List[List[int]]:
        res = float('inf')
        winner = root.val
        while root.left and root.right:
            if root.left.val > winner:
                res = min(res, root.left.val)
            elif root.right.val > winner:
                res = min(res, root.right.val)

            if root.left.val <= root.right.val:
                root = root.left
            else:
                root = root.right
        return res


    def test_1(self):
        self.assertEqual(3, self.secondMin(self.build_tree1()))

    def build_tree1(self):
        tree = nd.node(2)
        tree.left = nd.node(2)
        tree.right = nd.node(5)

        tree.left.left = nd.node(4)
        tree.left.right = nd.node(2)

        tree.right.left = nd.node(5)
        tree.right.right = nd.node(8)

        tree.left.right.left = nd.node(2)
        tree.left.right.right = nd.node(3)
        return tree