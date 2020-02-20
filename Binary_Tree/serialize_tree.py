# https://leetcode.com/problems/find-bottom-left-tree-value/
from typing import List

from Helpers import helper as hlp
from Helpers import test_class
from Helpers import node as nd
import collections


class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def serialize_dfs(self, root):
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
            else:
                res.append(None)
        while res[-1] is None:
            res.pop()
        return res

    def deserialize_dfs(self, array):
        #array = eval(data)
        array.reverse()

        def _deserialize(array):
            if not array:
                return None

            root = None
            value = array.pop()
            if value is not None:
                root = nd.node(value)
                root.left = _deserialize(array)
                root.right = _deserialize(array)
            return root

        return _deserialize(array)

    def serialize_level(self, root) -> int:
        queue = collections.deque()
        queue.append(root)
        res = []

        while queue:
            node = queue.popleft()
            if node:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append(None)

        while res and res[-1] is None:
            res.pop()
        return res

    def deserialize_level(self, data) -> int:
        data.reverse()

        root = nd.node(data.pop())
        dq = collections.deque([root])

        while data:
            node = dq.popleft()

            val = data.pop()
            if val is not None:
                node.left = nd.node(val)
                dq.append(node.left)

            if data:
                val = data.pop()
                if val is not None:
                    node.right = nd.node(val)
                    dq.append(node.right)

        return root

    def serialize2(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')

        vals = []
        doit(root)
        return ' '.join(vals)

    def test_z(self):
        array = self.serialize_dfs(self.build_tree1())
        self.assertEqual([1, 2, None, None, 3, 4, None, None, 5], array)
        root = self.deserialize_dfs(array)
        self.assertIsNotNone(root)

    def test_1(self):
        self.assertEqual([1, 2, 3, None, None, 4, 5], self.serialize(self.build_tree1()))

    def test_2(self):
        self.assertEqual(nd.node(1), self.deserialize([1, 2, 3, None, None, 4, 5]))

    def test_3(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], self.serialize(self.deserialize([1, 2, 3, 4, 5, 6, 7])))

    def build_tree1(self):
        tree = nd.node(1)
        tree.left = nd.node(2)
        tree.right = nd.node(3)

        tree.right.left = nd.node(4)
        tree.right.right = nd.node(5)
        return tree
