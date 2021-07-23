from typing import List


class Solution:

    def binary_search(self, nums, low, high, x):

        if high > low:
            mid = (high + low) // 2
            if nums[mid] == x:
                return mid
            elif nums[mid] > x:
                return self.binary_search(nums, low, mid, x)
            else:
                return self.binary_search(nums, mid + 1, high, x)
        else:
            return None

    def checkThreeSumComb(self, nums, i, k):
        if i + 1 >= k:
            return
        required_j = - (nums[i] + nums[k])
        j = self.binary_search(nums, i + 1, k, required_j)
        if j:
            self.result_list.append([nums[i], nums[j], nums[k]])
        return

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.result_list = []
        self.length = len(nums)
        if self.length < 3:
            return []

        k = self.length - 1
        while k > 2:
            i = 0
            while i < k:
                self.checkThreeSumComb(nums, i, k)
                i += 1
                while nums[i] == nums[i - 1] and i < k:
                    i += 1
            k -= 1
            while nums[k] == nums[k + 1] and k > 0:
                k -= 1

        return self.result_list
