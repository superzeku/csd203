class Node:
    def __init__(self,x):
        self.data = x
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head == None
    def insertLast(self,x):
        newNode = Node(x)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
            return
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode
    def insertFirst(self,x):
        newNode = Node(x)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
            return
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
    def insertAfter(self,d,x):
        if self.isEmpty():
            print("list is empty")
            return
        current = self.head
        while current.next is not None:
            if current.next == self.tail:
                self.insertLast(x)
                break
            if current.data == d:
                newNode = Node(x)
                newNode.prev = current
                newNode.next = current.next
                current.next.prev = newNode
                current.next = newNode
                break
            current = current.next

    def display(self):
        if self.isEmpty():
            print("list is empty")
            return
        print("head-->tail")
        current = self.head
        while current is not None:
            print(current.data,end = " ")
            current = current.next
        print("\ntail-->head")
        current = self.tail
        while current is not None:
            print(current.data,end = " ")
            current = current.prev
dllist = DoublyLinkedList()
for i in range(10):
    dllist.insertLast(i)
dllist.insertAfter(9,10)
dllist.display()