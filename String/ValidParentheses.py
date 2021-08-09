"""
Valid Parentheses:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

"""


class Solution:
    def isValid(self, s: str) -> bool:
        store = []
        for i in s:
            if i in ['(', '{', '[']:
                store.append(i)
            else:
                if len(store) == 0:
                    return False
                elif i == ')':
                    if store[-1] == '(':
                        store.pop()
                    else:
                        return False
                elif i == '}':
                    if store[-1] == '{':
                        store.pop()
                    else:
                        return False
                elif i == ']':
                    if store[-1] == '[':
                        store.pop()
                    else:
                        return False
        if len(store) == 0:
            return True
        return False
