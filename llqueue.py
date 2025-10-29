from singlylinkedlist import *
class LLQueue(SinglyLinkedList):
    def enqueue(self,x):
        self.insertLast(x)
    def dequeue(self):
        if self.isEmpty():
            return None
        tmp = self.head
        self.removeFirst()
        return tmp
    def front(self):
        if self.isEmpty():
            return None
        return self.head
# if __name__ == "__main__":    
#     lqueue = LLQueue()
#     for i in range(10): lqueue.enqueue(i)
#     lqueue.display()
#     node = lqueue.dequeue()
#     if node: print(node.data)