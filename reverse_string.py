
from Helpers import helper as hlp
from Helpers import test_class
import re

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def reverseString(self, s) -> None:
        i = len(s) - 1
        m = len(s) // 2
        j = 0
        while i >= m:
            s[i],s[j] = s[j],s[i]
            i -= 1
            j += 1

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

    def reverseString3(self, string):
        if not len(string):
            return string
        return self.reverseString3(string[1:]) + string[0]

    def test_1(self):
        self.assertEqual("ymar", self.reverseString3("ramy"))