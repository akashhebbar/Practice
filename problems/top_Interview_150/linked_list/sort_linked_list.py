class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head):
        # Handle empty list or single node
        if not head or not head.next:
            return head

        # Get length of linked list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # Bubble sort implementation
        for i in range(length):
            curr = head
            # Compare adjacent nodes
            for j in range(length - i - 1):
                if curr.val > curr.next.val:
                    # Swap values if current is greater than next
                    curr.val, curr.next.val = curr.next.val, curr.val
                curr = curr.next

        return head


# Test the solution
if __name__ == "__main__":
    # Create a linked list: 4 -> 2 -> 1 -> 3
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)

    solution = Solution()
    sorted_head = solution.sortList(head)
    print("Sorted linked list:")
    while sorted_head:
        print(sorted_head.val, end=" -> ")
        sorted_head = sorted_head.next
    print("None")
