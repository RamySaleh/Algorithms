
from Helpers import helper as hlp
from Helpers import test_class
import re

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def reverseString(self, string):
        res = ''

        i = len(string) - 1
        while i >= 0:
            print(string[i])
            res += string[i]
            i -= 1
        return res

    def reverseString2(self, string):
        res = ''
        stack = [string]

        while stack:
            curr = stack.pop()
            if curr:
                res += curr[-1]
                stack.append(curr[:-1])
        return res

    def test_1(self):
        self.assertEqual("ymar", self.reverseString2("ramy"))