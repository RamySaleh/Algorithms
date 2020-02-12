#https://leetcode.com/problems/binary-tree-upside-down/
import collections

from Helpers import helper as hlp
from Helpers import test_class
from Helpers import node as nd

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def upsideDownBinaryTree2(self, root: nd.node) -> nd.node:
        stack = [(root, False)]
        tree = []

        while stack:
            node,visited = stack.pop()

            if visited:
                tree.append(node.val)
            else:
                if node:
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))

        tree.reverse()
        root2 = nd.node(tree.pop())
        dq = collections.deque([root2])
        while tree:
            node = dq.popleft()
            if not node.right:
                node.right = nd.node(tree.pop())
                dq.append(node.right)
            if tree and not node.left:
                node.left = nd.node(tree.pop())
                dq.append(node.left)

        return root2

    def upsideDownBinaryTree(self, root):
        if not root or (not root.left and not root.right):
            return root

        left = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = root.right = None
        return left


    def test_1(self):
        self.assertEqual([4,5,2,None,None,3,1],hlp.tree_to_array(self.upsideDownBinaryTree(hlp.array_to_tree([1,2,3,4,5]))))

    def test_2(self):
        self.assertEqual([2,1],hlp.tree_to_array(self.upsideDownBinaryTree(hlp.array_to_tree([1,2]))))

    def test_3(self):
        self.assertEqual([3,None,2,None,1],hlp.tree_to_array(self.upsideDownBinaryTree(hlp.array_to_tree([1,2,None,3]))))