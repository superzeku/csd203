from llqueue import *
class PQueue(LLQueue):
    def enqueue(self,x):
        newNode = Node(x)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
            return
        current = self.head
        check = True
        while current.next is not None:
            if check and current.next.data > x:
                newNode.next = current.next
                current.next = newNode
                check = False
            current = current.next
        if check: current.next = self.tail = newNode
pqueue = PQueue()
for i in range(10): pqueue.enqueue(i)
pqueue.display()
pqueue.enqueue(5)
pqueue.display()