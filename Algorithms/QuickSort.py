class Solution:

    def getAndSetPivotIndex(self, nums, low, high):
        pivot = nums[high]
        i = low
        j = high - 1
        while i <= j:
            if nums[i] > pivot and nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            elif nums[i] <= pivot:
                i = i + 1
            elif nums[j] >= pivot:
                j = j - 1
        nums[i], nums[high] = nums[high], nums[i]
        return i

    def quickSort(self, nums, low, high):
        if len(nums) == 1:
            return nums
        if low < high:
            pivot_index = self.getAndSetPivotIndex(nums, low, high)

            self.quickSort(nums, low, pivot_index - 1)
            self.quickSort(nums, pivot_index + 1, high)
        return nums