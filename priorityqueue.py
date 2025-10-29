from llqueue import *
class PQueue(LLQueue):
    def __init__(self, reverse=False):
        super().__init__()
        self.reverse = reverse
    def enqueue(self,x):
        newNode = Node(x)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
            return
        current = self.head
        check = True
        while current.next is not None:
            if self.reverse: cond = current.next.data < x
            else: cond = current.next.data > x
            if check and cond:
                newNode.next = current.next
                current.next = newNode
                check = False
            current = current.next
        if check: current.next = self.tail = newNode
    def dequeue(self):
        if self.isEmpty():
            return None
        # luôn lấy phần tử đầu tiên (vì đã được sắp theo priority)
        x = self.head
        self.head = self.head.next
        return x

if __name__ == "__main__":
    pqueue = PQueue()
    for i in range(10): pqueue.enqueue(i)
    pqueue.display()
    pqueue.enqueue(5)
    pqueue.display()