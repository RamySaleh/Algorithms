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

        res = 0
        dic = {}
        for i in range(len(arr)):
            if self.valid(arr[i]):
                curr_str = arr[i]
            else:
                curr_str = ''
            for j in range(i, len(arr)):
                if self.valid(curr_str + arr[j]):
                    curr_str += arr[j]
                res = max(res, len(curr_str))
        return res

    def valid(self, str):
        dic = {}
        for c in str:
            if c in dic:
                return False
            else:
                dic[c] = ''
        return True

    def valid2(self, w1, w2):
        for c in w1:
            if c in w2:
                return False
        return True

    def maxLength2(self, arr: List[str]) -> int:
        l = 0
        cur_sum = 0
        res = 0
        dic = {}
        for r in range(len(arr)):
            cur_sum += len(arr[r])
            valid = self.isValid(arr[r], dic)
            if not valid:
                cur_sum -= len(arr[l])
                for c in arr[l]:
                    if c in dic: del dic[c]
                l += 1

            res = max(res, cur_sum)
            for c in arr[r]:
                dic[c] = ''

        return res

    def isValid(self, word, dic):
        for c in word:
            if c in dic:
                return False
        return True

    def test_1(self):
        self.assertEqual(4 ,self.maxLength(["un","iq","ue"]))

    def test_2(self):
        self.assertEqual(6 ,self.maxLength(["cha","r","act","ers"]))

    def test_3(self):
        self.assertEqual(16 ,self.maxLength(["jnfbyktlrqumowxd","mvhgcpxnjzrdei"]))

    def test_4(self):
        self.assertEqual(6 ,self.maxLength(["a", "abc", "d", "de", "def"]))

    def test_13(self):
        self.assertEqual(26 ,self.maxLength(["abcdefghijklm","bcdefghijklmn","cdefghijklmno","defghijklmnop","efghijklmnopq","fghijklmnopqr","ghijklmnopqrs","hijklmnopqrst","ijklmnopqrstu","jklmnopqrstuv","klmnopqrstuvw","lmnopqrstuvwx","mnopqrstuvwxy","nopqrstuvwxyz","opqrstuvwxyza","pqrstuvwxyzab"]))
