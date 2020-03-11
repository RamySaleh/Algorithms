# https://leetcode.com/problems/nested-list-weight-sum/

from Helpers import helper as hlp
from Helpers import test_class


class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def depthSum2(self, nestedList):
        return self.calSum(nestedList, 1, 0)

    def calSum(self, nestedList, depth, res):
        for item in nestedList:
            if isinstance(item, int):
                res += depth * item
            else:
                res = self.calSum(item, depth + 1, res)
        return res

    def depthSum(self, nestedList):
        res = 0
        stack = [(nestedList,1)]
        while stack:
            nestedList, depth = stack.pop()
            for item in nestedList:
                if isinstance(item, int):
                    res += depth * item
                else:
                    stack.append((item, depth + 1))
        return res

    def depthSumInverse(self, nestedList):
        res = 0
        self.m_depth = 0
        self.getMaxDepth(nestedList)
        stack = [(nestedList, self.m_depth)]
        while stack:
            nestedList, depth = stack.pop()
            for item in nestedList:
                if isinstance(item, int):
                    res += item * depth
                else:
                    stack.append((item, depth - 1))
        return res

    def getMaxDepth(self, nestedList, depth=1):
        self.m_depth = max(depth, self.m_depth)
        for item in nestedList:
            if not isinstance(item, int):
                self.getMaxDepth(item, depth + 1)

    def test_1(self):
        self.assertEqual(10, self.depthSum([[1, 1], 2, [1, 1]]))

    def test_2(self):
        self.assertEqual(12, self.depthSum([2, [1, 1], [1, 2]]))

    def test_inv_1(self):
        self.assertEqual(8, self.depthSumInverse([[1, 1], 2, [1, 1]]))

    def test_inv_2(self):
        self.assertEqual(17, self.depthSumInverse([1,[4,[6]]]))

    def test_inv_3(self):
        self.assertEqual(-3, self.depthSumInverse([[-1],[[-1]]]))
