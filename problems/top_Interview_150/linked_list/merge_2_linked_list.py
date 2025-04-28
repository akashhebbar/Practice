class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current != None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


obj1 = LinkedList()
obj2 = LinkedList()

obj1.insert_at_head(1)
obj1.insert_at_head(2)
obj1.insert_at_head(3)
obj1.insert_at_head(4)
obj1.insert_at_head(5)
obj1.print_list()

obj2.insert_at_head(2)
obj2.insert_at_head(4)
obj2.insert_at_head(5)
obj2.insert_at_head(6)
obj2.insert_at_head(8)
obj2.print_list()


def merge_2_linked_list(obj1, obj2):
    # Create a dummy node to handle edge cases
    dummy = Node(0)
    current = dummy

    current1 = obj1.head
    current2 = obj2.head

    # Compare and merge nodes
    while current1 and current2:
        if current1.value <= current2.value:
            current.next = current1
            current1 = current1.next
        else:
            current.next = current2
            current2 = current2.next
        current = current.next

    # Attach remaining nodes
    if current1:
        current.next = current1
    if current2:
        current.next = current2

    # Update obj1's head to point to the merged list
    obj1.head = dummy.next
    return obj1


merge_2_linked_list(obj1, obj2)
obj1.print_list()
