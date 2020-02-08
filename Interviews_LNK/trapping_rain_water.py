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
        water = 0
        l = 0
        r = len(height) - 1
        max_l = height[0]
        max_r = height[-1]

        while l <= r:
            # update left max
            max_l = max(max_l, height[l])
            # update right max
            max_r = max(max_r, height[r])

            # update water from the lower side
            if max_l <= max_r:
                water += max_l - height[l]
                l += 1
            else:
                water += max_r - height[r]
                r -= 1
        return water

    def trap_s(self, height):
        water = 0

        if len(height) < 3:
            return water

        for i,h in enumerate(height):
            max_l = self.get_max_l(i, height)
            max_r = self.get_max_r(i, height)
            cur_h = min(max_l, max_r) - h
            water += cur_h

        return water

    def get_max_l(self,i, height):
        max_l = 0
        while i >= 0:
            max_l = max(height[i], max_l)
            i -= 1

        return max_l

    def get_max_r(self, i, height):
        max_r = 0
        while i < len(height):
            max_r = max(height[i], max_r)
            i += 1

        return max_r

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

    def test_2(self):
        self.assertEqual(2, self.trap([2,0,2]))

    def test_t(self):
        self.assertEqual(2, self.trap(hlp.generate_array(1000,1000)))
