from typing import List
import math
from Helpers import profiler as prof
from Helpers import helper as hlp

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = math.ceil((end + start) / 2)
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1


def run(parms):
    print(Solution().search(parms[0], parms[1]))

input = [-1,0,3,5,9,12]
target = 3
prof.profile(run, input, target)