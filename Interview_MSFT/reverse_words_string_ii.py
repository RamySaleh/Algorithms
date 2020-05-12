from typing import List

from Helpers import helper as hlp
from Helpers import test_class
import random

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def reverseWords(self, s: List[str]) -> None:
        start = 0
        s.reverse()
        for i, c in enumerate(s):
            if c == " " or i + 1 == len(s):
                self.swap(s, start, i - 1 if i < len(s) - 1 else i)
                start = i + 1

    def swap(self, s, l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    def test_1(self):
        s = ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]
        self.reverseWords(s)
        self.assertEqual(["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"],s)
