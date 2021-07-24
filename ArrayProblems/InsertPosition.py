from typing import List


class Solution:
    def binarySearchPosition(self, nums, low, high, val):
        if high > low:
            mid = (high + low) // 2
            if nums[mid] == val:
                return mid
            elif val > nums[mid]:
                return self.binarySearchPosition(nums, mid + 1, high, val)
            else:
                return self.binarySearchPosition(nums, low, mid - 1, val)
        elif low == high:
            if nums[low] == val or val < nums[low]:
                return low
            elif val > nums[low]:
                return low + 1
        else:
            return low

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binarySearchPosition(nums, 0, len(nums) - 1, target)
