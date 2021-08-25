"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.


Example 1:

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        res = temp = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                new = l1.next
                temp.next = l1
                temp.next.next = None
                l1 = new
            else:
                new = l2.next
                temp.next = l2
                temp.next.next = None
                l2 = new
            temp = temp.next
        if l1:
            temp.next = l1
        if l2:
            temp.next = l2
        return res.next


