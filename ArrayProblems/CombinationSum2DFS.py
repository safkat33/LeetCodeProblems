from typing import List


class Solution:

    def checkCombinationDFS(self, arr, target, path, res):

        if target == 0:
            if path not in res:
                res.append(path)
                return
        else:
            for i in range(len(arr)):
                if arr[i] > target:
                    continue
                if i > 0:
                    if arr[i] == arr[i - 1]:
                        continue
                self.checkCombinationDFS(arr[i + 1:], target - arr[i], path + [arr[i]], res)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        while candidates[-1] > target:
            candidates.pop()
            if len(candidates) == 0:
                break
        self.checkCombinationDFS(candidates, target, [], res)
        return res
