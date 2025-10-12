class Node:
    def __init__(self,x):
        self.data = x
        self.next = None
    
class SinglyLinkedList:
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
        self.tail.next = newNode
        self.tail = newNode
    def insertFirst(self,x):
        newNode = Node(x)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
            return
        newNode.next = self.head
        self.head = newNode
    def removeFirst(self):
        if self.isEmpty():
            print("list is empty")
            return
        if self.head == self.tail:
            self.head = self.tail = None
            return
        current = self.head
        del self.head
        self.head = current.next
    def removeLast(self):
        if self.isEmpty():
            print("list is empty")
            return
        if self.head == self.tail:
            self.head = self.tail = None
            return
        current = self.head
        while current.next is not self.tail:
            current = current.next
        current.next = None
        self.tail = current
    def removeData(self,x):
        if self.isEmpty():
            print("list is empty")
            return
        if self.head.data == x:
            self.removeFirst()
            return
        current = self.head
        while current.next is not None:
            if current.next.data == x:
                current.next = current.next.next
                break
            current = current.next
        if current.next == self.tail:
            self.tail == current.next
    def display(self):
        if self.isEmpty():
            print("list is empty")
            return
        current = self.head
        while current is not None:
            print(current.data,end = " ")
            current = current.next
        print()
    def displayRecursion(self,x):
        if self.isEmpty():
            print("list is empty")
            return        
        if x is None: return
        print(x.data,end = " ")
        self.displayRecursion(x.next)
    def displayReverseRecursion(self,x):
        if self.isEmpty():
            print("list is empty")
            return
        if x is None: return
        self.displayReverseRecursion(x.next)
        print(x.data,end = " ")
if __name__ == "__main__":        
    llst = SinglyLinkedList()
    for i in range(10):
        llst.insertLast(i)
    llst.insertFirst(10)
    llst.removeFirst()
    llst.removeLast()
    llst.removeData(1)
    llst.display()
    llst.displayRecursion(llst.head)
    print()
    llst.displayReverseRecursion(llst.head)