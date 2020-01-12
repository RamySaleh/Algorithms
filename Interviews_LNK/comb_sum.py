#https://leetcode.com/explore/interview/card/linkedin/337/recursion-and-backtracking/2910/

from Helpers import helper as hlp
from Helpers import test_class
import re

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def combinationSum(self, candidates, target):
        res = []
        self.dfs(candidates, 0, target, [], res)
        return res

    def dfs(self, candidates, start, target, path, res):
        if target == 0:
            return res.append(path + [])

        for i in range(start, len(candidates)):
            if target - candidates[i] >= 0:
                path.append(candidates[i])
                self.dfs(candidates, i, target - candidates[i], path, res)
                path.pop()

    def test_1(self):
        self.assertEqual([[7],[2,2,3]], self.combinationSum([2,3,6,7], 7))