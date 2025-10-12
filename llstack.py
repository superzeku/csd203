from singlylinkedlist import *
class ListStack(SinglyLinkedList):
    def push(self,x):
        self.insertFirst(x)
    def pop(self):
        self.removeFirst()
    def top(self):
        if self.isEmpty():
            print("empty")
            return None
        return self.head.data
if __name__ == "__main__":
    lstack = ListStack()
    for i in range(10):
        lstack.push(i)
    lstack.pop()
    lstack.display()
    print(lstack.top())