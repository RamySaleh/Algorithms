#https://leetcode.com/problems/find-bottom-left-tree-value/
from typing import List

from Helpers import helper as hlp
from Helpers import test_class
from Helpers import node as nd
import collections

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def serialize(self, root) -> int:
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

        while not res[-1]:
            res.pop()
        return res

    def deserialize(self, data) -> int:
        data.reverse()

        root = nd.node(data.pop())
        queue = collections.deque([root])

        while data:
            node = queue.popleft()

            node.left = nd.node(data.pop())
            if node.left:
                queue.append(node.left)

            node.right = nd.node(data.pop())
            if node.right:
                queue.append(node.right)

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

    def deserialize2(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = nd.node(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()

    def test_1(self):
        self.assertEqual([1,2,3,None,None,4,5], self.serialize(self.build_tree1()))

    def test_2(self):
        self.assertEqual(nd.node(1), self.deserialize([1,2,3,None,None,4,5]))

    def test_3(self):
        self.assertEqual([1,2,3,4,5,6,7], self.serialize(self.deserialize([1,2,3,4,5,6,7])) )


    def build_tree1(self):
        tree = nd.node(1)
        tree.left = nd.node(2)
        tree.right = nd.node(3)

        tree.right.left = nd.node(4)
        tree.right.right = nd.node(5)
        return tree