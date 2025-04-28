# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # Initialize two pointers - slow and fast
        slow = fast = head

        # Move fast pointer twice as fast as slow pointer
        # When fast reaches the end, slow will be at the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


# Test cases
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    return "->".join(values)


# Test case 1: [1,2,3,4,5]
head1 = create_linked_list([1, 2, 3, 4, 5])
solution = Solution()
middle1 = solution.middleNode(head1)
print("Test case 1 [1,2,3,4,5]:")
print("Original list:", print_linked_list(head1))
print("Middle node value:", middle1.val)  # Should print 3

# Test case 2: [1,2,3,4,5,6]
head2 = create_linked_list([1, 2, 3, 4, 5, 6])
middle2 = solution.middleNode(head2)
print("\nTest case 2 [1,2,3,4,5,6]:")
print("Original list:", print_linked_list(head2))
print("Middle node value:", middle2.val)  # Should print 4
