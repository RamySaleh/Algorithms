from typing import List

class Solution:

    def __init__(self):
        self.cache = {}

    def pivotIndex(self, nums: List[int]) -> int:
        index = 0
        result = -1
        self.prepare_cache(nums)
        total_sum = self.cache[len(nums)]

        while index < len(nums):
            if index == 0:
                sumBefore = 0
            else:
                sumBefore = self.cache[index]

            sumAfter = total_sum - self.cache[index] - nums[index]
            #print(f"index={index} before={sumBefore} after={sumAfter}")

            if sumBefore == sumAfter:
                print(index)
                result = index
                break

            index = index + 1
        return result

    def prepare_cache(self, nums):
        sum = 0
        index = 1
        self.cache[0] = 0
        while index <= len(nums):
            sum = sum + nums[index - 1]
            self.cache[index] = sum
            index = index + 1

        #print(self.cache)


#Solution().pivotIndex([1, 2, 3, 4, 5, 1]) #3
#Solution().pivotIndex([-1,-1,-1,0,1,1]) #0
#Solution().pivotIndex([-1,-1,0,0,-1,-1]) #2
