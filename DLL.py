class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
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
            self.head.prev = node
            self.head = node
        self.size += 1

    def insert_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
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
            node.prev = current
            current.next.prev = node
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
            node.prev = prev
            current.prev.next = node
            current.prev = node
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
            self.head.prev = None
        self.size -= 1

    def delete_tail(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1

    def delete_node(self, node):
        if self.head is None:
            return
        if node == self.head:
            self.delete_head()
        elif node == self.tail:
            self.delete_tail()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
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
        return self

    def insert_sorted_helper(self, sorted_head, node):
        if sorted_head is None:
            node.next = None
            node.prev = None
            return node

        if node.data <= sorted_head.data:
            node.next = sorted_head
            node.prev = None
            sorted_head.prev = node
            return node

        current = sorted_head
        while current.next is not None and current.next.data < node.data:
            current = current.next

        node.next = current.next
        node.prev = current
        if current.next is not None:
            current.next.prev = node
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
   
if __name__ == '__main__':
    # create a new doubly linked list
    dll = DLL()

    # insert nodes at head, tail and position
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    dll.insert_head(node1)
    dll.insert_tail(node2)
    dll.insert(node3, 2)

    # insert nodes in sorted order
    node4 = Node(15)
    node5 = Node(25)
    node6 = Node(5)
    dll.sortedinsert(node4)
    dll.sortedinsert(node5)
    dll.sortedinsert(node6)

    # print the contents of the list
    dll.Print()

    # search for a node
    search_node = Node(30)
    result = dll.search(search_node)
    if result is not None:
        print("Node found: ", result.data)
    else:
        print("Node not found")

    # delete nodes
    dll.delete_head()
    dll.delete_tail()
    dll.delete_node(node4)

    # print the contents of the list
    dll.Print()

    # clear the list
    dll.clear()

    # print the contents of the list
    dll.Print()
