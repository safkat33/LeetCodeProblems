from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result_list = []
        length = len(nums)
        if length < 3:
            return []

        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, length - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    result_list.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j + 1] == nums[j]:
                        j += 1
                    j += 1
                    while k > j and nums[k - 1] == nums[k]:
                        k -= 1
                    k -= 1
        return result_list
