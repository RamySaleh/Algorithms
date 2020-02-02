#https://leetcode.com/problems/find-leaves-of-binary-tree/
from typing import List

from Helpers import helper as hlp
from Helpers import test_class
from Helpers import node as nd

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def isIdentical_itr(self, root1, root2) -> List[List[int]]:
        stack1 = [root1]
        stack2 = [root2]

        while stack1 and stack2:
            curr1 = stack1.pop()
            curr2 = stack2.pop()

            if not curr1 and not curr2:
                continue

            if (curr1 and not curr2) or (curr2 and not curr1) or (curr1.val != curr2.val):
                return False

            stack1.append(curr1.left)
            stack1.append(curr1.right)

            stack2.append(curr2.left)
            stack2.append(curr2.right)
        return True

    def isIdentical(self, root1, root2) -> List[List[int]]:
        return self.dfs(root1, root2)

    def dfs(self, root1, root2) -> List[List[int]]:
        if not root1 and not root2:
            return True

        if not root1 or not root2 or root1.val != root2.val:
            return False

        return self.dfs(root1.left, root2.left) and self.dfs(root1.right, root2.right)

    def test_1(self):
        self.assertEqual(True, self.isIdentical(self.build_tree1(),self.build_tree1()))

    def test_2(self):
        self.assertEqual(False, self.isIdentical(self.build_tree1(),self.build_tree2()))

    def test_1_1(self):
        self.assertEqual(True, self.isIdentical_itr(self.build_tree1(),self.build_tree1()))

    def test_2_1(self):
        self.assertEqual(False, self.isIdentical_itr(self.build_tree1(),self.build_tree2()))


    def build_tree1(self):
        tree = nd.node(1)
        tree.left = nd.node(2)
        tree.right = nd.node(3)

        tree.left.left = nd.node(4)
        tree.left.right = nd.node(5)
        return tree

    def build_tree2(self):
        tree = nd.node(1)
        tree.left = nd.node(2)
        tree.right = nd.node(3)

        tree.left.left = nd.node(6)
        tree.left.right = nd.node(5)
        return tree