class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_linked_list(head):
    previous = None
    while head:
        next_node = head.next
        head.next = previous
        previous = head
        head = next_node

    return previous


"""
[1->2->3->4->5]
"""

test = ListNode(1)
test.next = ListNode(2)
test.next.next = ListNode(3)
test.next.next.next = ListNode(4)
test.next.next.next.next = ListNode(5)

reversed_list = reverse_linked_list(test)
reversed_string = ""
while reversed_list:
    reversed_string += str(reversed_list.val)
    if reversed_list.next:
        reversed_string += "->"
    reversed_list = reversed_list.next
print(reversed_string)
