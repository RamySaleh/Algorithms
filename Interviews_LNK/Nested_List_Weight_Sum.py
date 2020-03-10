# https://leetcode.com/explore/interview/card/linkedin/339/array-and-strings/2907/

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


    def test_1(self):
        self.assertEqual(10, self.depthSum([[1, 1], 2, [1, 1]]))

    def test_2(self):
        self.assertEqual(12, self.depthSum([2, [1, 1], [1, 2]]))
