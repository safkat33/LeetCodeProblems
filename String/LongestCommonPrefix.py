"""
14. Longest Common Prefix

Share
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        if len(strs) == 1:
            return strs[0]
        strs.sort(key = len)
        for i in range(len(strs[0])):
            exist = False
            for j in range(1, len(strs)):
                if strs[0][i] == strs[j][i]:
                    exist = True
                else:
                    exist = False
                    break
            if exist:
                res += strs[0][i]
            else:
                break
        return res
