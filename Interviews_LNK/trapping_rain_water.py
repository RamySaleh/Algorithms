#https://leetcode.com/problems/trapping-rain-water/
from typing import List

from Helpers import helper as hlp
from Helpers import test_class

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def trap(self, height):
        if len(height) < 3:
            return 0
        res = 0
        l = 1
        r = len(height) - 2
        max_l = height[0]
        max_r = height[len(height) - 1]

        while l <= r:
            max_l = max(max_l, height[l])
            max_r = max(max_r, height[r])

            if max_l < max_r:
                res += max_l - height[l]
                l += 1
            else:
                res += max_r - height[r]
                r -= 1
        return res

    def trap2(self, height):
        stack = []
        water = 0

        for i in range(len(height)):
            # going up
            while len(stack) > 0 and height[stack[-1]] < height[i]:
                bottomHeight = height[stack.pop()]
                if len(stack) == 0:
                    break
                leftUpperIndex = stack[-1]
                heightDiff = min(height[leftUpperIndex], height[i]) - bottomHeight
                width = i - leftUpperIndex - 1
                water += heightDiff * width

            stack.append(i)

        return water


    def is_start(self, j, height, water_started):
        return height[j] > height[j + 1] and not water_started

    def test_1(self):
        self.assertEqual(6, self.trap([0,1,0,2,1,0,1,3,2,1,2,1]))