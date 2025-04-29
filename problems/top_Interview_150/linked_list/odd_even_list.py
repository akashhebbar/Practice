# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # Handle edge cases
        if not head or not head.next:
            return head

        # Initialize pointers
        odd = head
        even = head.next
        even_head = even  # Save the start of even list

        # Separate odd and even nodes
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        # Connect odd list to even list
        odd.next = even_head

        return head
