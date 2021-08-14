'''
Reorder List
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.


Example 1:

Input: head = [1,2,3,4,5]
Output: [1,4,2,3]
'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def splitList(head):
        fast = head
        slow = head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                slow = slow.next
        second_half = slow.next
        slow.next = None
        return head, second_half

    @staticmethod
    def reverse(head):
        previous = None
        current = head
        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt
        return previous

    @staticmethod
    def mergeList(first_half, second_half):

        current = first_half
        while current and second_half:
            new = second_half.next
            nxt = current.next
            current.next = second_half
            second_half.next = nxt
            second_half = new
            current = nxt
        return first_half

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return
        first_half, second_half = self.splitList(head)
        second_half = self.reverse(second_half)
        head = self.mergeList(first_half, second_half)
