from typing import List
import math
from Helpers import profiler as prof
from Helpers import helper as hlp

class Solution:

    def search(self, nums, target):
        if not nums:
            return -1

        s, e = 0, len(nums) - 1

        while s <= e:
            mid = math.ceil((s + e)/2)

            if target == nums[mid]:
                return mid

            if nums[s] <= nums[mid]:
                if nums[s] <= target <= nums[mid]:
                    e = mid - 1
                else:
                    s = mid + 1
            else:
                if nums[mid] <= target <= nums[e]:
                    s = mid + 1
                else:
                    e = mid - 1

        return -1

def run(parms):
    print(Solution().search(parms[0],parms[1]))

input = [4,5,6,7,0,1,2]
target = 0
prof.profile(run, input, target)