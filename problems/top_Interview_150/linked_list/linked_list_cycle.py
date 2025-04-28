# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        Detect if a linked list has a cycle using Floyd's Cycle-Finding Algorithm.

        Args:
            head: The head node of the linked list

        Returns:
            bool: True if there is a cycle, False otherwise
        """
        # If the list is empty or has only one node, there can't be a cycle
        if not head or not head.next:
            return False

        # Initialize two pointers: slow (tortoise) and fast (hare)
        slow = head
        fast = head

        # Move slow pointer by 1 and fast pointer by 2
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If they meet, there is a cycle
            if slow == fast:
                return True

        # If we reach here, fast pointer reached the end of the list
        return False


# Example usage
if __name__ == "__main__":
    # Create a linked list with a cycle
    # 1 -> 2 -> 3 -> 4
    #      ^         |
    #      |         v
    #      7 <- 6 <- 5

    # Create nodes
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)

    # Connect nodes
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node2  # Creates a cycle

    # Test the solution
    solution = Solution()
    print("Has cycle:", solution.hasCycle(node1))  # Should print: Has cycle: True

    # Create a linked list without a cycle
    # 1 -> 2 -> 3 -> 4 -> None
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = None

    print("Has cycle:", solution.hasCycle(node1))  # Should print: Has cycle: False
