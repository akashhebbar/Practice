class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_at_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def insert_after_node(self, value, target_value):
        new_node = Node(value)
        current = self.head

        while current != None:
            if current.value == target_value:
                new_node.next = current.next
                current.next = new_node
                self.size += 1
                return
            current = current.next
        print(f"Node with value {target_value} not found")

    def clear(self):
        self.head = None
        self.size = 0

    def delete_at_head(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next
        self.size -= 1

    def delete_at_tail(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
        self.size -= 1

    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty")
            return
        if self.head.value == value:
            self.head = self.head.next
            self.size -= 1
            return
        current = self.head
        while current != None:
            if current.next.value == value:
                current.next = current.next.next
                self.size -= 1
                return
            current = current.next
        print(f"Node with value {value} not found")

    def search(self, value):
        current = self.head
        while current != None:
            if current.value == value:
                return True
            current = current.next
        return False

    def reverse(self):
        prev = None
        current = self.head
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        return self

    def print_list(self):
        current = self.head
        while current != None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


Obj = LinkedList()
Obj.insert_at_head(1)
Obj.insert_at_head(2)
Obj.insert_at_head(3)
Obj.insert_at_head(4)
Obj.insert_at_head(5)
Obj.print_list()

Obj.reverse()
Obj.print_list()
