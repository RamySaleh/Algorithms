#https://leetcode.com/problems/shortest-word-distance-ii/
from typing import List

from Helpers import helper as hlp
from Helpers import test_class
import re

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        dic = {}
        minDistance = float("inf")
        l = 0
        for r in range(len(words)):
            w = words[r]
            self.addWord(w, dic)

            while word1 in dic and word2 in dic:
                currDistance = r - l
                minDistance = min(minDistance, currDistance)
                w = words[l]
                self.remWord(w, dic)
                l += 1

        return minDistance

    def addWord(self, w, dic):
        if w in dic:
            dic[w] += 1
        else:
            dic[w] = 1

    def remWord(self, w, dic):
        if dic[w] > 1:
            dic[w] -= 1
        else:
            del dic[w]

    def test_1(self):
        self.assertEqual(3, self.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"))

    def test_2(self):
        self.assertEqual(1, self.shortestDistance(["a", "c", "a", "b"], "a", "b"))