"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

practice
steps = |1|2|3|5|8
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        res = [1] * n
        for i in range(1, n):
            if i == 1:
                res[i] += res[i - 1]
            else:
                res[i] = res[i - 1] + res[i - 2]
        return res[-1]
