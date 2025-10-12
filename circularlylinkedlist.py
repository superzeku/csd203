class Node:
        def __init__(self,x):
            self.data = x
            self.next = None
class CircularlyLinkedList:
    def __init__(self):
        self.tail = None
    def isEmpty(self):
        return self.tail == None
    def insertFirst(self,x):
        newNode = Node(x)
        if self.isEmpty():
            self.tail = newNode
            self.tail.next = self.tail
            return
        newNode.next = self.tail.next 
        self.tail.next = newNode
    def insertLast(self,x):
        self.insertFirst(x)
        self.tail = self.tail.next
    def removeFirst(self):
        if self.isEmpty():
            print("Empty")
            return
        if self.tail.next == self.tail:
            self.tail = None
            return
        self.tail.next = self.tail.next.next
    def removeLast(self):
        if self.isEmpty():
            print("Empty")
            return
        if self.tail.next == self.tail:
            self.tail = None
            return
        current = self.tail.next
        while current.next != self.tail:
            current = current.next
        current.next = self.tail.next
        self.tail = current
    def disp(self):
        if self.isEmpty():
            print("Empty")
            return
        current = self.tail.next
        while current != self.tail:
            print(current.data, end = " ")
            current = current.next
        print(current.data)
cll = CircularlyLinkedList()
for i in range(10): cll.insertLast(i)
cll.removeLast()
cll.disp()