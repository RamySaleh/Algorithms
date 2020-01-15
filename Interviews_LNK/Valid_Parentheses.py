#https://leetcode.com/explore/interview/card/linkedin/336/heap-queue-stack/1958/

from Helpers import helper as hlp
from Helpers import test_class
import re

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {'}': '{', ')': '(', ']': '['}
        open_chars = ['{', '(', '[']
        for c in s:
            if c in open_chars:
                stack.append(c)
            elif c in lookup:
                if not stack:
                    return False
                opening_char = stack.pop()
                if opening_char != lookup[c]:
                    return False

        return not stack

    def test_1(self):
        self.assertEqual(True, self.isValid('{([])}'))

    def test_2(self):
        self.assertEqual(False, self.isValid('{([])'))