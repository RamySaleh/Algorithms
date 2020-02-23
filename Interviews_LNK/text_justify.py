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
        return res + [' '.join(cur).ljust(maxWidth)]

    def fullJustify2(self, words, maxWidth):
        i, N, result = 0, len(words), []
        while i < N:
            # decide how many words to be put in one line
            oneLine, j, currWidth, positionNum, spaceNum = [words[i]], i + 1, len(words[i]), 0, maxWidth - len(words[i])
            while j < N and currWidth + 1 + len(words[j]) <= maxWidth:
                oneLine.append(words[j])
                currWidth += 1 + len(words[j])
                spaceNum -= len(words[j])
                positionNum, j = positionNum + 1, j + 1
            i = j
            # decide the layout of one line
            if i < N and positionNum:
                spaces = [' ' * (spaceNum / positionNum + (k < spaceNum % positionNum)) for k in range(positionNum)] + [
                    '']
            else:  # last line or the line only has one word
                spaces = [' '] * positionNum + [' ' * (maxWidth - currWidth)]
            result.append(''.join([s for pair in zip(oneLine, spaces) for s in pair]))
        return result

    def test_1(self):
        self.assertEqual(["What   must   be", "acknowledgment  ", "shall be        "],
                         self.fullJustify(["What","must","be","acknowledgment","shall","be"],16))