class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_duplicates(head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            # Skip the duplicate node
            current.next = current.next.next
        else:
            # Move to the next distinct element
            current = current.next
    return head


# Helper function to create a linked list from a list
def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


# Helper function to print linked list
def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)


# Example Usage
head = create_linked_list([1, 1, 2, 3, 3])
new_head = delete_duplicates(head)
print_linked_list(new_head)
