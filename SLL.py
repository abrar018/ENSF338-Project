class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        self.size = 0 if head is None else 1

    def insert_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def insert_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insert(self, node, position):
        if position == 1:
            self.insert_head(node)
        elif position == self.size+1:
            self.insert_tail(node)
        elif position < 1 or position > self.size+1:
            print("Invalid position")
        else:
            current = self.head
            for i in range(1, position-1):
                current = current.next
            node.next = current.next
            current.next = node
            self.size += 1

    def sortedinsert(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            self.size = 1
        else:
            if self.is_sorted():
                self.insert_sorted(node)
            else:
                self.sort()
                self.insert_sorted(node)

    def is_sorted(self):
        current = self.head
        while current is not None and current.next is not None:
            if current.data > current.next.data:
                return False
            current = current.next
        return True


    def insert_sorted(self, node):
        current = self.head
        prev = None
        while current is not None and current.data < node.data:
            prev = current
            current = current.next
        if prev is None:
            self.insert_head(node)
        elif current is None:
            self.insert_tail(node)
        else:
            node.next = current
            prev.next = node
            self.size += 1

    def search(self, node):
        current = self.head
        while current is not None:
            if current.data == node.data:
                return current
            current = current.next
        return None

    def delete_head(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.size -= 1

    def delete_tail(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = None
            self.tail = current
        self.size -= 1

    def delete_node(self, node):
        if self.head is None:
            return
        if node == self.head:
            self.delete_head()
        elif node == self.tail:
            self.delete_tail()
        else:
            current = self.head
            while current.next != node:
                current = current.next
            current.next = node.next
            self.size -= 1

    def sort(self):
        if self.head is None or self.head == self.tail:
            return
        sorted_head = None
        current = self.head
        while current is not None:
            next_node = current.next
            sorted_head = self.insert_sorted_helper(sorted_head, current)
            current = next_node
        self.head = sorted_head
        
        # find the new tail node
        self.tail = self.head
        while self.tail.next is not None:
            self.tail = self.tail.next
    
    def insert_sorted_helper(self, sorted_head, node):
        if sorted_head is None:
            node.next = None
            return node

        if node.data <= sorted_head.data:
            node.next = sorted_head
            return node

        current = sorted_head
        while current.next is not None and current.next.data < node.data:
            current = current.next

        node.next = current.next
        current.next = node
        return sorted_head
    
    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def Print(self):
        print("The length of the list is", self.size)
        if self.is_sorted():
            print("The list is sorted")
        else:
            print("The list is not sorted")
        current = self.head
        print("The contents of the list are:", end=" ")
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()
        print()

if __name__ == "__main__":
    sll = SLL()
    sll.Print()
    sll.insert_head(Node(1))
    sll.insert_head(Node(2))
    sll.insert_head(Node(3))
    sll.insert_head(Node(4))
    sll.Print()
    sll.insert_tail(Node(5))
    sll.insert_tail(Node(6))
    sll.insert_tail(Node(7))
    sll.insert_tail(Node(8))
    sll.Print()
    sll.insert(Node(9), 1)
    sll.insert(Node(10), 5)
    sll.insert(Node(11), 9)
    sll.insert(Node(12), 13)
    sll.Print()
    sll.delete_head()
    sll.delete_tail()
    sll.delete_node(sll.search(Node(6)))
    sll.Print()
    sll.clear()
    sll.Print()
    sll.insert_head(Node(1))
    sll.insert_head(Node(3))
    sll.insert_head(Node(2))
    sll.insert_head(Node(4))
    sll.Print()
    sll.sort()
    sll.Print()
    sll.insert_sorted(Node(5))
    sll.Print()
    sll.insert_sorted(Node(0))
    sll.Print()
    sll.insert_sorted(Node(3))
    sll.Print()
    sll.clear()
    sll.Print()
    sll.sortedinsert(Node(1))
    sll.sortedinsert(Node(3))
    sll.sortedinsert(Node(2))
    sll.sortedinsert(Node(4))
    sll.Print()
    sll.sortedinsert(Node(5))
    sll.Print()
    sll.sortedinsert(Node(0))
    sll.Print()
    sll.sortedinsert(Node(3))
    sll.Print()

