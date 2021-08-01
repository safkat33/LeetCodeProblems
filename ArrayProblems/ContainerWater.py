'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.



Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
'''

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        avg_max_height = 0
        l = 0
        while l < len(height ) -1:
            if height[l] == 0:
                l += 1
                continue
            if l > 0:
                prev_height = height[ l -1]
                while height[l] <= prev_height:
                    l += 1
                    if l == len(height ) -1:
                        break

            if height[l] < avg_max_height:
                l += 1
                continue
            r = len(height ) -1
            while r > l:
                if height[r] == 0:
                    r -= 1
                    continue
                if r < len(height ) -1:
                    prev_height = height[ r +1]
                    while r > l:
                        if height[r] <= avg_max_height:
                            height[r] = 0
                            r -= 1
                        else:
                            break
                width = r- l
                height_lr = min(height[l], height[r])
                if width * height_lr > max_area:
                    max_area = width * height_lr
                    avg_max_height = height_lr
                r -= 1
            l += 1
        return max_area
