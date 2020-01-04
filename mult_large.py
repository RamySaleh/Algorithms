from Helpers import profiler as prof
from Helpers import helper as hlp


class Solution:

    def __init__(self):
        self.lookup = {}

    def mult(self, n: int, m: int) -> int:
        return 0

def run(parms):
    sl = Solution()

    res = sl.fib(parms[0], parms[1])
    print(res)

prof.profile(run, 45, 11)
