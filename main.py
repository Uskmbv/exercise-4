#1

class SinglyLinkedList:

    def clear(self):
        self.head = None
        self.size = 0

#2

class SinglyLinkedList:

    def get_data(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return data
            current = current.next
        return False

#3

def insert(self, prev_data, data):
    new_node = SLLNode(data)
    current = self.head
    while current is not None:
        if current.data == prev_data:
            new_node.next = current.next
            current.next = new_node
            self.size += 1
            return True
        current = current.next
    return False

#4
def delete_node(self, data):
    if self.head is None:
        return
    if self.head.data == data:
        self.head = self.head.next
        self.size -= 1
        return
    current = self.head
    while current.next is not None:
        if current.next.data == data:
            current.next = current.next.next
            self.size -= 1
            return
        current = current.next

#5

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insert_node(self, prev_node_data, new_node_data):
        node = Node(new_node_data)
        current = self.head
        while current:
            if current.data == prev_node_data:
                node.prev = current
                node.next = current.next
                if current.next:
                    current.next.prev = node
                current.next = node
                self.size += 1
                return
            current = current.next
        print(f"{prev_node_data} not found in list")

    def delete_node(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev is None:  # element to delete is the head
                    self.head = current.next
                else:
                    current.prev.next = current.next
                if current.next is None:  # element to delete is the tail
                    self.tail = current.prev
                else:
                    current.next.prev = current.prev
                self.size -= 1
                return
            current = current.next
        print(f"{data} not found in list")

    def get_data(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return False

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

#6

def push(self, element):
    self.stack.append(element)

def pop(self):
    if len(self.stack) == 0:
        return None
    return self.stack.pop()

def top(self):
    if len(self.stack) == 0:
        return None
    return self.stack[-1]

def size(self):
    return len(self.stack)

#7

class MyQueue:
    def __init__(self):
        self.queue = []

    def add(self, element):
        self.queue.append(element)

    def remove(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return None
        return self.queue.pop(0)

    def show_left(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return None
        return self.queue[0]

    def show_right(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return None
        return self.queue[-1]

    def size(self):
        return len(self.queue)



