from typing import List

from Helpers import helper as hlp
from Helpers import test_class
import random

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def reverseWords(self, s: str) -> str:
        words = s.strip().split(' ')
        words.reverse()
        return ' '.join(filter(lambda w: w != '',words))

    def test_1(self):
        self.assertEqual('blue is sky the',self.reverseWords('the sky is blue'))

    def test_2(self):
        self.assertEqual('world! hello',self.reverseWords('  hello world!  '))

    def test_3(self):
        self.assertEqual('example good a',self.reverseWords('a good   example'))
