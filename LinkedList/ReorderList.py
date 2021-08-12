'''
Reorder List
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.


Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]
'''


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getLastNode(self, head, last=None):
        while head.next:
            prev = head
            last = head.next
            head = head.next
        prev.next = None
        return last

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        current = head
        while current:
            if current.next:
                nxt = current.next
                if nxt.next:
                    last = self.getLastNode(current)
                    current.next = last
                    last.next = nxt
                    current = nxt
                else:
                    break
            else:
                current = current.next



