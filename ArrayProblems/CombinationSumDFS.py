from typing import List


class Solution:

    def __init__(self):
        self.result = []

    def dfs(self, arr, target, path):
        if target < 0:
            return
        elif target == 0:
            self.result.append(path)
            return
        else:
            for i in range(len(arr)):
                if arr[i] <= target:
                    self.dfs(arr[i:], target - arr[i], path + [arr[i]])

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.dfs(candidates, target, [])
        return self.result
