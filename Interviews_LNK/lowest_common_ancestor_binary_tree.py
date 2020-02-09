#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

from Helpers import helper as hlp
from Helpers import test_class
from Helpers import node as nd

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        self.dfs(root, p, q)
        return self.ans

    def dfs(self, current_node, p, q):
        if not current_node:
            return False

        # If the current node is one of p or q
        mid = current_node.val == p.val or current_node.val == q.val

        left = self.dfs(current_node.left, p, q)
        right = self.dfs(current_node.right, p, q)

        if mid and left or mid and right or left and right:
            self.ans = current_node.val

        # Return True if either of the three bool values is True.
        return mid or left or right

    def test_1(self):
        self.assertEqual(3, self.lowestCommonAncestor(hlp.array_to_tree([3,5,1,6,2,0,8,None,None,7,4]),nd.node(5), nd.node(1)))

    def test_2(self):
        self.assertEqual(5, self.lowestCommonAncestor(hlp.array_to_tree([3,5,1,6,2,0,8,None,None,7,4]),
                                                          nd.node(5), nd.node(4)))