#https://leetcode.com/explore/interview/card/linkedin/337/recursion-and-backtracking/2910/

from Helpers import helper as hlp
from Helpers import test_class
import re

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def combinationSum(self, candidates, target):
        res = []
        self.dfs(candidates, 0, 0,target, [],res)
        return res

    def dfs(self, candidates, index, sum, target, path, res):
        if sum == target:
            res.append(path)
            return

        if sum > target:
            return

        for i in range(index, len(candidates)):
            self.dfs(candidates, i, sum + candidates[i], target, path + [candidates[i]], res)


    def test_1(self):
        self.assertEqual([[7],[2,2,3]], self.combinationSum([2,3,6,7], 7))