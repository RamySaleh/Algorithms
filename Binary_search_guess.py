from typing import List
import math
from Helpers import profiler as prof
from Helpers import helper as hlp

class Solution:
    pick = 6
    def guessNumber(self, n: int) -> int:
        s = 0
        e = n

        while s <= e:
            m = math.ceil((s + e) / 2)
            g = self.guess(m)
            if g == 0:
                return m
            elif g == 1:
                e = m - 1
            elif g == -1:
                s = m + 1

    def guess(self, number):
        if number == Solution.pick:
            return 0
        elif number > Solution.pick:
            return 1
        else:
            return -1

def run(parms):
    print(Solution().guessNumber(parms[0]))

target = 10
prof.profile(run, target)