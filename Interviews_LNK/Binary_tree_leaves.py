#https://leetcode.com/problems/find-leaves-of-binary-tree/
from typing import List

from Helpers import helper as hlp
from Helpers import test_class
from Helpers import node as nd

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def findLeaves(self, root) -> List[List[int]]:
        res = []
        if not root:
            return res

        while root.left or root.right:
            res_loop = []
            self.dfs(None, root, False, res_loop)
            res.append(res_loop)
        res.append([root.val])
        return res

    def dfs(self, parent, root, isLeft, res):
        if not root:
            return

        # leaf
        if not root.left and not root.right:
            res.append(root.val)
            if parent:
                if isLeft:
                    parent.left = None
                else:
                    parent.right = None
            return

        self.dfs(root, root.left, True, res)
        self.dfs(root, root.right, False, res)

    def test_1(self):
        self.assertEqual([[4,5,3],[2],[1]], self.findLeaves(self.build_tree1()))


    def build_tree1(self):
        tree = nd.node(1)
        tree.left = nd.node(2)
        tree.right = nd.node(3)

        tree.left.left = nd.node(4)
        tree.left.right = nd.node(5)
        return tree