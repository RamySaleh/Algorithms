from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest_number = 0
        largest_number_index = 0
        for i in range(len(nums)):
            if nums[i] > largest_number:
                largest_number = nums[i]
                largest_number_index = i

        #print(f"largest={largest_number} index={largest_number_index}")
        is_more_than_double = True
        for n in nums:
            if n != largest_number and n * 2 > largest_number:
                is_more_than_double = False
                break

        if is_more_than_double:
            return largest_number_index
        else:
            return -1


r = Solution().dominantIndex([0,0,0,1])
#r = Solution().dominantIndex([3,6,1,0])
print(r)