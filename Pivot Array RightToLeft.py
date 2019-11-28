from typing import List

class Solution:

    def __init__(self):
        self.cache = {}

    def pivotIndex(self, nums: List[int]) -> int:
        index = len(nums)
        result = -1
        self.prepare_cache(nums)

        while index >= 1:
            if index == 1:
                sumBefore = 0
            else:
                sumBefore = self.cache[index - 1]

            sumAfter = self.cache[len(nums)] - self.cache[index]
            #print(f"index={index - 1} before={sumBefore} after={sumAfter}")

            if sumBefore == sumAfter:
                print(index-1)
                result = index-1

            index = index - 1
        return result

    def prepare_cache(self, nums):
        sum = 0
        index = 1
        while index <= len(nums):
            sum = sum + nums[index - 1]
            self.cache[index] = sum
            index = index + 1
            #print(self.cache)


#Solution().pivotIndex([1, 2, 3, 4, 5, 1]) #3
#Solution().pivotIndex([-1,-1,-1,0,1,1]) #0
Solution().pivotIndex([-1,-1,0,0,-1,-1]) #2
