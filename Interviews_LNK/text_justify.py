#https://leetcode.com/explore/interview/card/linkedin/339/array-and-strings/1968/

from Helpers import helper as hlp
from Helpers import test_class
import re

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def fullJustify(self, words, maxWidth):
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        return res + [''.join(cur).ljust(maxWidth)]

    def test_1(self):
        self.assertEqual(["What   must   be", "acknowledgment  ", "shall be        "],
                         self.fullJustify(["What","must","be","acknowledgment","shall","be"],16))