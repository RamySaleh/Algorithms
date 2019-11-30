from typing import List
import math
from Helpers import profiler as prof
from Helpers import helper as hlp

class Solution:
    def sqrt(self, target: int) -> int:
        start = 0
        end = target

        while start <= end:
            mid = math.ceil((end + start) / 2)
            sqr = mid * mid
            next_sqr = (mid+1) * (mid+1)
            if sqr <= target < next_sqr:
                return mid
            elif sqr > target:
                end = mid - 1
            elif sqr < target:
                start = mid + 1
        return 0

    def sqrt2(self, x):
        for i in range(x):
            sqr = i * i
            next_sqr = (i + 1) * (i + 1)
            if sqr <= x < next_sqr:
                return i

def run(parms):
    print(Solution().sqrt2(parms[0]))

target = 15000000
prof.profile(run, target)