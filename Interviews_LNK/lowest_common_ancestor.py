#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

from Helpers import helper as hlp
from Helpers import test_class
from Helpers import node as nd

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def lowestCommonAncestor2(self, root, p, q):
        parent_val = root.val
        p_val = p.val
        q_val = q.val

        # If both p and q are greater than parent
        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        # If both p and q are lesser than parent
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        # We have found the split point, i.e. the LCA node.
        else:
            return root.val

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]

        while stack:
            node = stack.pop()

            if node:
                if p.val > node.val and q.val > node.val:
                    stack.append(node.right)
                elif p.val < node.val and q.val < node.val:
                    stack.append(node.left)
                else:
                    return node.val


    def test_1(self):
        self.assertEqual(6, self.lowestCommonAncestor(hlp.array_to_tree([6,2,8,0,4,7,9,None,None,3,5]),nd.node(2), nd.node(8)))

    def test_2(self):
        self.assertEqual(2, self.lowestCommonAncestor(hlp.array_to_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),
                                                          nd.node(2), nd.node(4)))