#https://leetcode.com/problems/minimum-window-substring/
import collections
from typing import List

from Helpers import helper as hlp
from Helpers import test_class

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def minWindow2(self, s, t):
        if not t or not s:
            return ""

        # Dictionary which keeps a count of all the unique characters in t.
        dict_t = collections.Counter(t)

        # Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)

        # left and right pointer
        l, r = 0, 0

        # formed is used to keep track of how many unique characters in t are
        # present in the current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C.
        # Thus formed would be = 3 when all these conditions are met.
        formed = 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):

            # Add one character from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            # If the frequency of the current character added equals to
            # the desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                l += 1

                # Keep expanding the window once we are done contracting.
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]

    def minWindow(self, s, t):
        if not t or not s:
            return ""

        dicT = collections.Counter(t)

        window = {}
        minDistance = float("inf")
        l = 0
        ans = None
        for r in range(len(s)):  # enlarge window from the right
            c = s[r]
            window[c] = window.get(c, 0) + 1

            while self.containsString(dicT, window):  # as long as desirable
                # the enhancement condition
                currDistance = r - l
                if currDistance < minDistance:
                    minDistance = currDistance
                    ans = [l,r + 1]

                # retract window from the left
                c = s[l]
                window[c] -= 1
                l += 1

        return s[ans[0]: ans[1]] if ans else ""

    def containsString(self, dicT, dicS):
        for c,count in dicT.items():
            if c not in dicS or dicS[c] < count:
                return False
        return True

    def containsString2(self, t, dic):
        for c in t:
            if c not in dic:
                return False
        return True

    def test_1(self):
        self.assertEqual("BANC", self.minWindow("ADOBECODEBANCD","ABC"))

    def test_2(self):
        self.assertEqual("aa", self.minWindow("aa","aa"))

    def test_3(self):
        self.assertEqual("a", self.minWindow("a","a"))

    def test_4(self):
        self.assertEqual("", self.minWindow("a","aa"))