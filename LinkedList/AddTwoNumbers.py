'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res_node = ListNode()
        sum = l1.val + l2.val
        res_node.val = sum % 10
        sub_res_node = ListNode()
        leading = sum // 10
        if leading > 0:
            sub_res_node.val = leading
            res_node.next = sub_res_node
        elif l1.next is not None or l2.next is not None:
            res_node.next = sub_res_node
        l1 = l1.next
        l2 = l2.next
        while (l1 is not None or l2 is not None):
            if l1 is None:
                sum = l2.val + sub_res_node.val
                sub_res_node.val = sum % 10
                leading = sum // 10
                sub_node = ListNode()
                if leading > 0:
                    sub_node.val = leading
                    sub_res_node.next = sub_node
                elif l2.next is not None:
                    sub_res_node.next = sub_node
                l2 = l2.next
                sub_res_node = sub_res_node.next
                continue
            elif l2 is None:
                sum = l1.val + sub_res_node.val
                sub_res_node.val = sum % 10
                leading = sum // 10
                sub_node = ListNode()
                if leading > 0:
                    sub_node.val = leading
                    sub_res_node.next = sub_node
                elif l1.next is not None:
                    sub_res_node.next = sub_node
                l1 = l1.next
                sub_res_node = sub_res_node.next
                continue
            else:
                sum = l1.val + l2.val + sub_res_node.val
                sub_res_node.val = sum % 10
                leading = sum // 10
                sub_node = ListNode()
                if leading > 0:
                    sub_node.val = leading
                    sub_res_node.next = sub_node
                elif l1.next is not None or l2.next is not None:
                    sub_res_node.next = sub_node
                sub_res_node = sub_res_node.next
            l1 = l1.next
            l2 = l2.next
        return res_node
