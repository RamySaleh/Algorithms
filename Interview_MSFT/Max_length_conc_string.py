# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

from Helpers import helper as hlp
from Helpers import test_class
from typing import List


class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def maxLength(self, arr: List[str]) -> int:
        if len(arr) == 1:
            return len(arr[0])
        self.res = 0
        self.perms = []
        for i in range(len(arr)):
            if self.valid(arr[i]):
                self.dfs(arr, arr[i], i + 1)

        return self.res

    def dfs(self, arr, str, i):
        self.perms.append(str)
        self.res = max(self.res, len(str))
        for j in range(i, len(arr)):
            if self.valid(str + arr[j]):
                self.dfs(arr, str + arr[j], j + 1)

    def valid(self, str):
        dic = {}
        for c in str:
            if c in dic:
                return False
            else:
                dic[c] = ''
        return True


    def test_1(self):
        self.assertEqual(4 ,self.maxLength(["un","iq","ue"]))

    def test_2(self):
        self.assertEqual(6 ,self.maxLength(["cha","r","act","ers"]))

    def test_3(self):
        self.assertEqual(16 ,self.maxLength(["jnfbyktlrqumowxd","mvhgcpxnjzrdei"]))

    def test_4(self):
        self.assertEqual(6 ,self.maxLength(["a", "abc", "d", "de", "def"]))

    def test_12(self):
        self.assertEqual(16 ,self.maxLength(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]))

    def test_13(self):
        self.assertEqual(26 ,self.maxLength(["abcdefghijklm","bcdefghijklmn","cdefghijklmno","defghijklmnop","efghijklmnopq","fghijklmnopqr","ghijklmnopqrs","hijklmnopqrst","ijklmnopqrstu","jklmnopqrstuv","klmnopqrstuvw","lmnopqrstuvwx","mnopqrstuvwxy","nopqrstuvwxyz","opqrstuvwxyza","pqrstuvwxyzab"]))
