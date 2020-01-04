from Helpers import profiler as prof
from Helpers import helper as hlp


class Solution:

    def __init__(self):
        self.lookup = {}

    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        if n - 1 not in self.lookup:
            self.lookup[n - 1] = self.fib(n - 1)

        if n - 2 not in self.lookup:
            self.lookup[n - 2] = self.fib(n - 2)

        return self.lookup[n - 1] + self.lookup[n - 2]

def run(parms):
    sl = Solution()

    res = sl.fib(parms[0])
    print(res)

prof.profile(run, 4)
