#https://leetcode.com/problems/longest-valid-parentheses/submissions/
import math

from Helpers import helper as hlp
from Helpers import test_class
import re

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        longest = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                stack.pop()
                if not stack:  # unmatched closing
                    stack.append(i)
                else:  #
                    longest = max(i - stack[-1], longest)

        return longest

    def longestValidParentheses2(self, s: str) -> int:
        stack = [-1]
        counter = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    counter = max(counter, i - stack[-1])
        return counter

    def test_1(self):
        self.assertEqual(2, self.longestValidParentheses('(()('))

    def test_2(self):
        self.assertEqual(6, self.longestValidParentheses('()(())'))

    def test_3(self):
        self.assertEqual(2, self.longestValidParentheses('()(()'))

    def test_4(self):
        self.assertEqual(2, self.longestValidParentheses('()'))

    def test_5(self):
        self.assertEqual(4, self.longestValidParentheses(')()())'))