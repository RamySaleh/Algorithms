#https://leetcode.com/explore/interview/card/linkedin/336/heap-queue-stack/1959/

from Helpers import helper as hlp
from Helpers import test_class
import re

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def evalRPN(self, tokens) -> int:
        stack = []
        operators = ['+', '-', '/', '*']

        for n in tokens:
            if n in operators:
                n1 = stack.pop()
                n2 = stack.pop()
                res = None
                if n == '+':
                    res = n2 + n1
                elif n == '-':
                    res = n2 - n1
                elif n == '/':
                    res = int(n2 / n1)
                elif n == '*':
                    res = n2 * n1
                stack.append(res)
            else:
                stack.append(int(n))
        return stack.pop()

    def test_1(self):
        self.assertEqual(9, self.evalRPN(["2", "1", "+", "3", "*"]))

    def test_2(self):
        self.assertEqual(22, self.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))