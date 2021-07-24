from typing import List


class Solution:

    def __init__(self):
        self.result = []

    def addCombination(self, candidates, i, j, target):
        arr = []
        if i == j:
            if target % candidates[i] == 0:
                i_times = target // candidates[i]
                for x in range(i_times):
                    arr.append(candidates[i])
                self.result.append(arr)
        else:
            i_times = (target // candidates[i]) - 1
            while i_times > 0:
                arr_multy = []
                if i == 1:
                    print(i_times)
                if (target - (candidates[i] * i_times)) % candidates[j] == 0:
                    j_times = (target - (candidates[i] * i_times)) // candidates[j]

                    for x in range(i_times):
                        arr_multy.append(candidates[i])
                    for y in range(j_times):
                        arr_multy.append(candidates[j])
                    self.result.append(arr_multy)

                i_times -= 1

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        for i in range(len(candidates)):
            if candidates[i] <= target:
                for j in range(i, len(candidates)):
                    if candidates[j] <= target:
                        self.addCombination(candidates, i, j, target)

        return self.result
