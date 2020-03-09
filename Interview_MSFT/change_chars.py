from typing import List

from Helpers import helper as hlp
from Helpers import test_class
import random

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def getString(self, riddle):
        # write your code in Python 3.6
        letters = 'abcdefghijklmnopqrstuvwxyz'
        s = list(riddle)
        before = None
        for i in range(len(s)):
            if s[i] == '?':
                char = None
                while not char or not self.validChar(before, char, i, s):
                    char = random.choice(letters)
                    s[i] = char
            before = s[i]
        res = ''.join(s)
        return res

    def validChar2(self,char, i, s):
        if len(s) == 1:
            return True
        elif i == 0 and i + 1 < len(s) and char == s[i + 1]:
            return False
        elif i == len(s) - 1 and char == s[i - 1]:
            return False
        elif 0 < i < len(s) - 1 and (char == s[i - 1] or char == s[i + 1]):
            return False

        return True

    def validChar(self, before,char, i, s):
        if len(s) == 1:
            return True
        elif not before and i + 1 < len(s) and char == s[i + 1]:
            return False
        elif i == len(s) - 1 and char == s[i - 1]:
            return False
        elif 0 < i < len(s) - 1 and (char == s[i - 1] or char == s[i + 1]):
            return False

        return True

    def test_1(self):
        self.assertEqual(True,self.isValid(self.getString('a?b')))

    def test_2(self):
        self.assertEqual(True,self.isValid(self.getString('ab?')))

    def test_3(self):
        self.assertEqual(True,self.isValid(self.getString('?ab')))

    def test_4(self):
        self.assertEqual(True,self.isValid(self.getString('a????b')))

    def test_4a(self):
        self.assertEqual(True,self.isValid(self.getString('ab?ac?')))

    def test_5(self):
        self.assertEqual(True,self.isValid(self.getString('a??????????')))

    def test_6(self):
        self.assertEqual(True,self.isValid(self.getString('??????????abv')))

    def test_7(self):
        self.assertEqual(True,self.isValid(self.getString('????')))

    def test_8(self):
        self.assertEqual(True,self.isValid(self.getString('?')))

    def test_9(self):
        self.assertEqual(True,self.isValid(self.getString('')))

    def test_10(self):
        self.assertEqual(True,self.isValid(self.getString('f')))

    def test_11(self):
        self.assertEqual(True,self.isValid(self.getString('abcdefghijkl??opqrstuvwxyz')))

    def test_z(self):
        self.assertEqual(True,self.isValid(self.getString('a???????????????????b')))


    def isValid(self, str):
        last = None
        for i in range(len(str)):
            if str[i] == '?' or str[i] == last:
                return False
        return True
