#https://leetcode.com/explore/interview/card/linkedin/341/trees-and-graphs/1983/
import collections

from Helpers import helper as hlp
from Helpers import test_class
import re

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def ladderLength(self, beginWord: str, endWord: str, wordList):
        queue = collections.deque([[beginWord, 1]])
        chars = 'abcdefghijklmnopqrstuvwxyz'
        wordList = set(wordList)

        while queue:
            word, level = queue.popleft()
            if word == endWord:
                return level

            for i in range(len(word)):
                for c in chars:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in wordList:
                        queue.append((new_word, level + 1))
                        wordList.remove(new_word)
        return 0


    def test_1(self):
        self.assertEqual(5, self.ladderLength('hit', 'cog',["hot","dot","dog","lot","log","cog"]))

    def test_2(self):
        self.assertEqual(5, self.ladderLength('qa', 'sq',["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]))