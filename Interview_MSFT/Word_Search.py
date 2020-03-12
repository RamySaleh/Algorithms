# https://leetcode.com/problems/word-search/

from Helpers import helper as hlp
from Helpers import test_class
from typing import List


class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def exist(self, board: List[List[str]], word: str):
        if not board:
            return False
        h = len(board)
        w = len(board[0])
        for r in range(h):
            for c in range(w):
                if board[r][c] == word[0]:
                    found = self.walk(r, c, board, 0, word)
                    if found:
                        return True
        return False

    def walk(self, r, c, board, i, word):
        if not (0 <= r < len(board)) or not (0 <= c < len(board[0])) \
                or board[r][c] != word[i] or board[r][c] == '?':
            return

        temp = board[r][c]
        board[r][c] = '?'
        if i == len(word) - 1:
            return True

        res = self.walk(r, c + 1, board, i + 1, word) or \
              self.walk(r, c - 1, board, i + 1, word) or \
              self.walk(r + 1, c, board, i + 1, word) or \
              self.walk(r - 1, c, board, i + 1, word)

        if not res:
            board[r][c] = temp
        return res

    def test_1(self):
        self.assertTrue(self.exist([['A', 'B', 'C', 'E'],
                                    ['S', 'F', 'C', 'S'],
                                    ['A', 'D', 'E', 'E']], "ABCCED"))

    def test_2(self):
        self.assertTrue(self.exist([['A', 'B', 'C', 'E'],
                                    ['S', 'F', 'C', 'S'],
                                    ['A', 'D', 'E', 'E']], "SEE"))

    def test_3(self):
        self.assertFalse(self.exist([['A', 'B', 'C', 'E'],
                                     ['S', 'F', 'C', 'S'],
                                     ['A', 'D', 'E', 'E']], "ABCB"))

    def test_4(self):
        self.assertFalse(self.exist([["a", "b"], ["c", "d"]], "abcd"))

    def test_5(self):
        self.assertTrue(self.exist([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB"))

    def test_6(self):
        self.assertTrue(self.exist([["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], "ABCESEEEFS"))

    def test_7a(self):
        self.assertFalse(self.exist([["A", "A", "C"], ["A", "A", "E"], ["F", "D", "E"]], "AAAAAAAAAAAAA"))

    def test_7(self):
        self.assertFalse(
            self.exist([["a", "a", "a", "a"], ["a", "a", "a", "a"], ["a", "a", "a", "a"]], "aaaaaaaaaaaaa"))
