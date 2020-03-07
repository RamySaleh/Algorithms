from typing import List

from Helpers import helper as hlp
from Helpers import test_class
import random

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def getString(self, str):
        dic = self.buildDic(str)
        letters = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(len(str)):
            if str[i] == '?':
                char = None
                while not char or not self.validChar(char, i, str, dic):
                    char = random.choice(letters)
                str = str[:i] + char + str[i + 1:]
                dic[str[i]] = None
        print(str)
        return str

    def buildDic(self, str):
        dic = {}
        for c in str:
            if c != '?':
                dic[c] = None
        return dic

    def validChar(self,char, i, str, dic):
        if char in dic:
            return False
        elif i == 0 and i + 1 < len(str) and char == str[i + 1]:
            return False
        elif i == len(str) - 1 and char == str[i - 1]:
            return False
        elif 0 < i < len(str) - 1 and (char == str[i - 1] or char == str[i + 1]):
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
