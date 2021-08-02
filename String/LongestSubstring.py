'''
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checked = set()
        total = 0
        for i in range(len(s)):
            checked.clear()
            checked.add(s[i])
            subtotal = 1
            for j in range(i + 1, len(s)):
                if s[j] not in checked:
                    subtotal += 1
                    checked.add(s[j])
                else:
                    break
            total = max(total, subtotal)
            if len(s) - i < total:
                checked.clear()
                break
        return total
