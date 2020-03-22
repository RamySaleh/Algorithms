# https://leetcode.com/problems/string-to-integer-atoi/
from typing import List

from Helpers import helper as hlp
from Helpers import test_class
import random


class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def myAtoi(self, str: str):
        res = 0
        allowed = ['-', '+']
        str = str.strip()

        if not str or (str[0] != '+' and str[0] != '-') and not str[0].isdigit():
            return res

        clean_str = ''
        for i in range(0, len(str)):
            if str[i].isdigit():
                clean_str += str[i]
            elif str[i] in allowed:
                if i == 0:
                    clean_str += str[i]
                else:
                    break
            else:
                break

        if not clean_str or (len(clean_str) == 1 and clean_str[0] in allowed):
            return res

        res = int(clean_str)
        if res < 0:
            res = max(res, -2147483648)
        else:
            res = min(res, 2147483647)
        return res

    def test_1(self):
        self.assertEqual(-42, self.myAtoi('   -42'))

    def test_2(self):
        self.assertEqual(4193, self.myAtoi('4193 with words'))

    def test_3(self):
        self.assertEqual(-2147483648, self.myAtoi('-91283472332'))

    def test_4(self):
        self.assertEqual(3, self.myAtoi('3.14159'))

    def test_4(self):
        self.assertEqual(3, self.myAtoi('3.14159'))
